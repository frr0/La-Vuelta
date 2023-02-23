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
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from testScript import *

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




link='https://www.lavuelta.es/en/rankings'
readDataFromWeb(link)


stage=writeDataInDictionary()

#a cosa serve sta roba sotto?

#abc = ""
#n = 10
#m = 0
 
#for line in lines:
#    line2 = line.text.replace("\n", " ").replace("\n\n\n\n", "").replace("      ", ",").replace("   ", ",").replace("  ", ",").replace(",,,,,,,,,,,,,", ",").replace(",,,,,,,,,,,,,,,,", ",").replace(",,,,",",").replace(",,,",",").replace(",,",",")
#    if m < n:
#        abc = abc + "\n" + line2
#        m = m + 1
#

for nn in stage:
    if nn < 21:
        ran = ran + "\n" + str(stage[nn].get("rank")) + " " + stage[nn].get("name") + " " + str(stage[nn].get("gap"))
        nn = nn + 1
    else:
        break
print("\n\n\n\n\n\n")
print(ran)

# here are the dictionary of the teams

team1,team2,T1,T2=readTeamsData()       #T1,2 sono le stringhe  team1,2 sono i dizionari

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
T2 = T2 + "\n\nPoints: " + str(pt2)


with open('Points.txt', 'a', newline='',encoding="utf-8") as f:
    f.write(str(pt1)+'\n'+str(pt2)+'\n')
            
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


        
