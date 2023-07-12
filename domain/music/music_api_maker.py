import schedule
from bs4 import BeautifulSoup as bs
import requests
import time
import json
import re


def getData(music, dataList):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = 'https://www.melon.com/song/detail.htm?songId=' + music
    html = requests.get(url, headers=headers).text
    soup = bs(html, 'html.parser')

    title = soup.find('div', {'class': 'song_name'})
    title.find('strong').decompose()

    for br in soup.find('div', {'class': 'lyric'}).find_all('br'):
        br.replace_with("\n ")

    dataDict = {
        'id': music,
        'image': soup.find('a', {'class': 'image_typeAll'}).find('img')['src'],
        'title': title.text.strip(),
        'artist': soup.find('a', {'class': 'artist_name'}).find('span').text.strip(),
        'album': soup.find('dl', {'class': 'list'}).find_all('dd')[0].text.strip(),
        'date': soup.find('dl', {'class': 'list'}).find_all('dd')[1].text.strip(),
        'genre': soup.find('dl', {'class': 'list'}).find_all('dd')[2].text.strip(),
        'des': soup.find('div', {'class': 'lyric'}).text.strip()
    }

    dataList.append(dataDict)


def getList():
    dataList = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = "https://www.melon.com/chart/index.htm"
    html = requests.get(url, headers=headers).text
    soup = bs(html, 'html.parser')

    music_list = soup.find_all('tr', {'class': 'lst50'})[:20]

    for music in music_list:
        reg = re.compile('\(([^)]+)')
        music = reg.findall(music.find_all("td")[4].find("a")["href"])[0].replace("'", "")

        getData(music, dataList)

    file_path = "domain/music/models/music_data.json"

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dataList, file, indent=2, ensure_ascii=False)


getList()

schedule.every().day.at("01:00").do(getList)

while True:
    schedule.run_pending()
    time.sleep(1)
