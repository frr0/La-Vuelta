from cgi import print_arguments
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from collections import OrderedDict
import requests
import sys

import json
import f
# Content of f.py
# # Module: f.py
# from telegram.ext.updater import Updater
# updater = Updater("Token", use_context=True)

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

t_1 = "/team1"
t_2 = "/team2"
t_3 = "/ranking"

PT1 = 0
PT2 = 0

def start(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(t_1)], [KeyboardButton(t_2)], [KeyboardButton(t_3)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, welcome to the unofficial La Vuelta bot.", reply_markup=ReplyKeyboardMarkup(buttons))
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
    /team1      - t1
    /team2      - t2
    /ranking- ranking""")
    
    
def team_1(update: Update, context: CallbackContext):
    update.message.reply_text(PT1 + T1)

def team_2(update: Update, context: CallbackContext):
    update.message.reply_text(PT2 + T2)

def ranking(update: Update, context: CallbackContext):
    # rk = " "+(str(abc))
    print(abc)
    update.message.reply_text(ran)
    # update.message.reply_text(abc)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


abc = ""
T1 = "Team1:\n"
T2 = "Team2:\n"

# Making a GET request
r = requests.get('https://www.lavuelta.es/en/rankings')

# create webdriver object
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get("https://www.lavuelta.es/en/rankings")
  
# get element 
element = driver.find_element_by_link_text("GENERAL RANKING")
  
# create action chain object
action = ActionChains(driver)
  
# click the item
action.click(on_element = element)
  
# perform the operation
action.perform()

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='sticky-scroll')

lines = s.find_all('tr')
for line in lines:
    print(line.text.replace("\n", " ").replace("\n\n\n\n", "").replace("      ", ",").replace("   ", ",").replace("  ", ",").replace(",,,,,,,,,,,,,", ",").replace(",,,,,,,,,,,,,,,,", ",").replace(",,,,",",").replace(",,,",",").replace(",,",","))
 
n = 10
m = 0
 
# here you collect the arrival position and time of the stage

i = 0
ran = ""
stage = {}
file = open('ranking.txt', 'r')
for line in file:
    pos    = line.rstrip().split(',')
    if i == 0:
        pos = ""
        i = i + 1
        continue
    rank   = int(pos[0])
    name   = pos[1]
    num    = pos[2]
    team   = pos[3]
    time   = pos[4]
    gap    = pos[5]
    bonus  = pos[6]

    if rank == 1:
        points = 100
    elif rank == 2:
        points = 50
    elif rank == 3:
        points = 20
    else:
        points = 0

    cyclist = {
        'rank': rank,
        'name': name,
        'num': num,
        'team': team,
        'time': time,
        'gap': gap,
        'bonus': bonus,
        'points': points
    }
    stage[i] = cyclist
    i = i + 1
file.close()

for line in lines:
    line2 = line.text.replace("\n", " ").replace("\n\n\n\n", "").replace("      ", ",").replace("   ", ",").replace("  ", ",").replace(",,,,,,,,,,,,,", ",").replace(",,,,,,,,,,,,,,,,", ",").replace(",,,,",",").replace(",,,",",").replace(",,",",")
    if m < n:
        abc = abc + "\n" + line2
        m = m + 1


for nn in stage:
    if nn < 21:
        ran = ran + "\n" + str(stage[nn].get("rank")) + " " + stage[nn].get("name") + " " + str(stage[nn].get("gap"))
        nn = nn + 1
    else:
        break
print("\n\n\n\n\n\n")
print(ran)

# here are the dictionary of the teams

team1 = {}
file = open('team1.txt', 'r')
a = 0
for line in file:
    name    = line.rstrip()
    team1[a] = name
    T1 = T1 + "\n" + name
    a = a + 1
file.close()

team2 = {}
file = open('team2.txt', 'r')
b = 0
for line in file:
    name    = line.rstrip()
    team2[b] = name
    T2 = T2 + "\n" + name
    b = b + 1
file.close()

# here the points

pt1 = 0
pt2 = 0

for x in stage:
    for t1 in team1:
        if team1[t1] == stage[x].get("name"):
            pt1 = pt1 + stage[x].get("points")
    for t2 in team2:
        if team2[t2] == stage[x].get("name"):
            pt2 = pt2 + stage[x].get("points")
            
T1 = T1 + "\n\nPoints: " + str(pt1)
print(str(pt1)+'\n', file=open('Points.txt', 'a'))
T2 = T2 + "\n\nPoints: " + str(pt2)
print(str(pt2)+'\n', file=open('Points.txt', 'a'))
            
# print()
# print()
# print("team1 points:")
# print(pt1)
# print("team1 points:")
# print(pt2)

f.updater.dispatcher.add_handler(CommandHandler('start', start))
f.updater.dispatcher.add_handler(CommandHandler('team1', team_1))
f.updater.dispatcher.add_handler(CommandHandler('team2', team_2))
f.updater.dispatcher.add_handler(CommandHandler('ranking', ranking))
f.updater.dispatcher.add_handler(CommandHandler('help', help))
f.updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
f.updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
f.updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
f.updater.start_polling()


        
