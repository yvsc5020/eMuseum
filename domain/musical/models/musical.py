import json
from bs4 import BeautifulSoup as bs
import requests


def getList():
    with open('domain/musical/models/musical_data.json') as f:
        data = json.load(f)

    return data
