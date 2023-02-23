import requests
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def readDataFromWebWithCSV(link):
    #link='https://www.lavuelta.es/en/rankings'
    chrome_driver=ChromeDriverManager().install()
    driver=Chrome(service=Service(chrome_driver))
    driver.maximize_window()
    driver.get(link)


    # get element 
    driver.find_element(By.XPATH,"//button[contains(text(),'General ranking')]").click()



    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')


    
    s = soup.find('div', class_='sticky-scroll')

    table=s.find('table')

    rows = table.find_all('tr')
    #data is a list that contains all the lines of the table, each line is a list of field
    data=[]
    for row in rows:
            titles=row.find_all('th')
            titles = [title.text.strip().replace(' ','') for title in titles]

            data.append(titles)

            cols = row.find_all('td')
            cols = [col.text.strip().replace(' ','') for col in cols]

            data.append(cols)

     #write on table excell
    with open('output.csv', 'w', newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


#per fare il csv avevo tolto tutti gli spazi quindi da ora tutti doppi nomi/cognomi sono attaccati
    reader = csv.reader(open('output.csv', 'r'))
    lr=list(reader)
    writer = open('ranking.txt', 'w')


    for line in lr:
        if(len(line)==0):
            continue
        for field in range(len(line)-1):
            writer.write(line[field]+" ")
        writer.write('\n')

    writer.close()

def readDataFromWeb(link):
    link='https://www.lavuelta.es/en/rankings'
    chrome_driver=ChromeDriverManager().install()
    driver=Chrome(service=Service(chrome_driver))
    driver.maximize_window()
    driver.get(link)
    # get element 
    driver.find_element(By.XPATH,"//button[contains(text(),'General ranking')]").click()

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    
    s = soup.find('div', class_='sticky-scroll')

    table=s.find('table')

    rows = table.find_all('tr')
    #data is a list that contains all the lines of the table, each line is a list of field
    data=[]
    for row in rows:
            titles=row.find_all('th')
            titles = [title.text.strip() for title in titles]

          
            
            data.append(titles)

            cols = row.find_all('td')
           
            cols = [col.text.strip() for col in cols]
            

            data.append(cols)

    writer = open('ranking.txt', 'w',encoding="utf-8")

   #elimino le liste vuote che non so perchè vengono create
    for list in data:
        if(len(list)==0):
            data.remove(list)
   
    
    for line in data:
        if(len(line)==0):
            continue
        for field in line:

            writer.write(field+',')

        writer.write('\n')   
         


    writer.close()

def writeDataInDictionary():
     # here you collect the arrival position and time of the stage
    i=0
    stage = {}
    file = open('ranking.txt', 'r')

    
    lines=file.readlines()
    
    for line in lines:
        if i == 0:
            pos = ""
            i = i + 1
            continue
        
        pos = line.rstrip().split(',')
        
        
        
       
        rank   =int(pos[0])
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
    return(stage)




def readTeamsData():
    # here are the dictionary of the teams
    T1 = "Team1:"
    T2 = "Team2:"

    team1 = {}
    file = open('team1.txt', 'r',encoding="utf-8")
    a = 0
    for line in file.readlines():
        name    = line.rstrip()
        team1[a] = name
        T1 = T1 + "\n" + name
        a = a + 1
    file.close()

    team2 = {}
    file = open('team2.txt', 'r',encoding="utf-8")
    b = 0
    for line in file.readlines():
        name    = line.rstrip()
        team2[b] = name
        T2 = T2 + "\n" + name
        b = b + 1
    file.close()


    return team1,team2,T1,T2








