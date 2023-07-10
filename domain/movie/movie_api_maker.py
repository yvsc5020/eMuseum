import schedule
from bs4 import BeautifulSoup as bs
import requests
import time
import json


def getData(movie, dataList):
    dataDict = {
        'id': movie.find('a')['href'].split('midx=')[1],
        'title': movie.find('strong', {'class': 'title'}).text.strip(),
        'image': movie.find('img')['src'],
        'ratio': movie.find('strong', {'class': 'percent'}).find('span').text.strip(),
    }

    url = 'http://www.cgv.co.kr/movies/detail-view/?midx=' + dataDict['id']
    html = requests.get(url).text
    soup = bs(html, 'html.parser')

    dataDict['status'] = '상영중' if soup.find('em', {'class': 'lightblue'}) is not None \
        else soup.find('em', {'class': 'red'}).text.strip()
    dataDict['genre'] = soup.find('div', {'class': 'spec'}).find_all('dt')[2].text.strip()\
        .replace('장르 :', '').replace(' ', ' ').replace('/ 기본 정보 :', '')

    actor = ""
    for idx, a in enumerate(soup.find('dd', {'class': 'on'}).find_all('a')[:3]):
        actor += a.text.strip()
        if idx + 1 != len(soup.find('dd', {'class': 'on'}).find_all('a')[:3]):
            actor += ", "
    dataDict['actor'] = actor

    dataDict['director'] = soup.find('div', {'class': 'spec'}).find('dd').find('a').text.strip()
    dataDict['des'] = soup.find('div', {'class': 'sect-story-movie'}).text.strip().replace('\n', ' ').replace('  ', ' ')

    dataList.append(dataDict)


def getList():
    dataList = []

    url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
    html = requests.get(url).text
    soup = bs(html, 'html.parser')

    movie_list = soup.find('div', {'class': 'sect-movie-chart'}).select('ol > li')[:7]

    for movie in movie_list:
        getData(movie, dataList)

    file_path = "domain/movie/models/movie_data.json"

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dataList, file, indent=2, ensure_ascii=False)


schedule.every().day.at("01:00").do(getList)

while True:
    schedule.run_pending()
    time.sleep(1)
