import json


def getList():
    with open('domain/music/models/music_data.json', encoding='UTF8') as f:
        data = json.load(f)

    return data
