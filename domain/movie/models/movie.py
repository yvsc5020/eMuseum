import json


def getList():
    with open('domain/movie/models/movie_data.json', encoding='UTF8') as f:
        data = json.load(f)

    return data
