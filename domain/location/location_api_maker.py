import googlemaps
from models import key
import json

gmaps = googlemaps.Client(key=key.getKey())

place_list = {'museum': ['국립중앙박물관', '국립고궁박물관', '국립국악원', '국립민속박물관', '대한민국역사박물관'],
              'art': ['국립극장', '예술의전당', '정동극장', '국립현대미술관 서울'],
              'book': ['국립세종도서관', '국립중앙도서관', '국립어린이청소년도서관'],
              'movie': ['대한극장', '인디스페이스', '필름포럼', '이봄씨어터', '시티렉스']}

dataList = []

for place_key in place_list:
    for place in place_list[place_key]:
        result = gmaps.geocode(place, language='ko')[0]
        dataList.append({'type': place_key, 'name': place, 'address': result['formatted_address'],
                         'location': result['geometry']['location']})

file_path = "domain/location/models/location_data.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(dataList, file, indent=2, ensure_ascii=False)
