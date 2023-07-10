import json
from bs4 import BeautifulSoup as bs
import requests


def getList():
    with open('domain/theater/models/theater_data.json') as f:
        data = json.load(f)

    return data


def getDetail(id):
    url = "https://www.ntok.go.kr/kr/Ticket/Performance/Details?performanceId=" + id
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/109.0.0.0 Safari/537.36"}

    html = requests.get(url, headers).text
    soup = bs(html, 'html.parser')

    prd_txt = soup.find("div", {"class": "prd_txt"})

    return prd_txt.text.strip()
