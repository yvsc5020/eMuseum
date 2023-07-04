import json


def getList():
    with open('domain/theater/models/theater_data.json') as f:
        data = json.load(f)

    return data


def getDetail(id):
    return "good"
