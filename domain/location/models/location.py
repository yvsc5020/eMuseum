import json


def getList():
    with open('domain/location/models/location_data.json', encoding='UTF8') as f:
        data = json.load(f)

    return data
