import schedule
from bs4 import BeautifulSoup as bs
import requests
import time
import json
import re


def getData(game, dataList):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = 'https://www.gamemeca.com/' + game
    html = requests.get(url, headers=headers).text
    soup = bs(html, 'html.parser')

    dataDict = {
        'title': soup.find('h2', {'class': 'h_gm'}).text.strip(),
        'genre': soup.find_all('li', {'class': 'rightA'})[1].text.strip(),
        'make': soup.find_all('li', {'class': 'rightA'})[2].text.strip(),
        'service': soup.find_all('li', {'class': 'rightA'})[3].text.strip(),
        'age': soup.find_all('li', {'class': 'rightA'})[4].text.strip(),
        'date': soup.find_all('li', {'class': 'rightA'})[5].text.strip(),
        'des': soup.find('div', 'db-cont1-left').text.strip()
    }

    dataList.append(dataDict)


def getList():
    dataList = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = "https://www.gamemeca.com/ranking.php"
    html = requests.get(url, headers=headers).text
    soup = bs(html, 'html.parser')

    game_list = soup.find_all('tr', {'class': 'ranking-table-rows'})[:20]

    for game in game_list:
        game = game.find("a")["href"]

        getData(game, dataList)

    file_path = "domain/game/models/game_data.json"

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dataList, file, indent=2, ensure_ascii=False)


getList()

schedule.every().day.at("01:00").do(getList)

while True:
    schedule.run_pending()
    time.sleep(1)
