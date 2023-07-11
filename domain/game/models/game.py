import json


def getList():
    with open('domain/game/models/game_data.json', encoding='UTF8') as f:
        data = json.load(f)

    return data
