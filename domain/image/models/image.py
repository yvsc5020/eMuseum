from PIL import Image
import tensorflow as tf
import numpy as np
import io
import requests
from bs4 import BeautifulSoup as bs
import re


def getResult(file):
    img = Image.open(io.BytesIO(file))
    img_resize = img.resize((300, 300))

    img_array = tf.keras.utils.img_to_array(img_resize)
    img_array = tf.expand_dims(img_array, 0)

    model = tf.keras.models.load_model('domain/image/models/eMuseum.h5')

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ['bronze_mirror', 'cannon', 'check_rain', 'gold_crown', 'gold_shoes',
                   'king_chair', 'not_skatch_bowl', 'old_josun_bronze_sword', 'skatch_bowl',
                   'stone_stele', 'stone_sword', 'sun_watch', 'temple_stele', 'ten_stonetower']
    kor_name = {
        'bronze_mirror': ['청동거울', '/relic/search/view?relicId=4380'],
        'check_rain': ['측우기', '/showroom/759/view?relicId=757'],
        'ten_stonetower': ['경천사 십층석탑', '/relic/search/view?relicId=4334'],
        'gold_crown': ['금관', '/relic/search/view?relicId=159727'],
        'king_chair': ['근정전 어좌', '/showroom/759/view?relicId=16224'],
        'gold_shoes': ['식리총 금동신발', '/showroom/760/view?relicId=87'],
        'stone_stele': ['진흥왕 순수비', '/relic/search/view?relicId=2483'],
        'stone_sword': ['돌칼', '/showroom/760/view?relicId=12007'],
        'not_skatch_bowl': ['민무늬토기', '/relic/search/view?relicId=2179'],
        'skatch_bowl': ['빗살무늬토기', '/showroom/760/view?relicId=11161'],
        'old_josun_bronze_sword': ['고조선 청동검', '/relic/search/view?relicId=1996'],
        'sun_watch': ['앙부일구', '/relic/search/view?relicId=2399'],
        'temple_stele': ['원랑선사_탑비', 'relic/search/view?relicId=4363'],
        'cannon': ['운현궁 화포', '/relic/search/view?relicId=4480'],
    }
    eng_name = class_names[np.argmax(score)]
    name = kor_name[eng_name][0]

    url = "https://www.museum.go.kr/site/main" + kor_name[eng_name][1]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/109.0.0.0 Safari/537.36"}

    html = requests.get(url, headers).text
    soup = bs(html, 'html.parser')

    reg = re.compile('\(([^)]+)')
    img = reg.findall(str(soup.find("div", {"class": "swiper-slide"})))[0].replace("'", "")

    reg = re.compile('^\/relic')
    if reg.match(img) is not None:
        img = "https://www.museum.go.kr" + img

    des = soup.find("div", {"class": "view-info-cont"}).find('p').text.strip()

    eng_des = {
        'bronze_mirror': 'This is a bronze mirror from a group of bronze artifacts excavated from Daegok-ri, '
                         'Dogok-myeon, Hwasun-gun, Jeollanam-do. The surface of the mirror is smooth. The mirror back '
                         'is surrounded by a prominent rim that is semicircular in cross-section and has two '
                         'ring-shaped taps slightly upward from the center. The pattern on the mirror back is a '
                         'highly elaborate geometric pattern based on triangles and circles.',
        'check_rain': 'It is believed to have been made during the time of King Sejong, as it belonged to the '
                      'Kansanggam, a government office in charge of astronomy, geography, and bookkeeping during the '
                      'Joseon Dynasty. The geodesic on top of the geodesic table is the Geumyeong Geodesic, '
                      'which was made in 1837 by Geumyeong, a princess who was the governor of Chungcheongnam-do. It '
                      'is the only geodesic that has survived to this day. During the Joseon Dynasty, rain gauges '
                      'were made centrally and sent to not only the Chungcheonggamyeong but also to the gaengyongs in '
                      'the eight provinces, and observers in each region reported rainfall to the center.',
        'ten_stonetower': '',
        'gold_crown': "It was discovered in 1921 in Geumgwanchong, Noseo-dong, Gyeongju, Gyeongsangbuk-do. About 10,"
                      "000 items, including pure gold products, earthenware, bronze, jade, and weapons, "
                      "were unearthed at Geumgwanchong, but it was this gold pipe that attracted the most attention. "
                      "It was worn by an undertaker in a wooden coffin. The tomb is believed to be a royal tomb due "
                      "to the large size of the tomb and the quality and quantity of the burial items. Therefore, "
                      "it is highly likely that this crown was worn by a king. A total of six solid gold crowns have "
                      "been unearthed in Gyeongju tombs so far, and this one is the most representative, supporting "
                      "this assumption. The rim is made of thin gold plates cut out, and the inscription is set on "
                      "top. The front is decorated with a stylized stele, and the back is decorated with two rhombic "
                      "stelae. In each position, there were regular rows of jade balls and lingzhi (瓔珞). On the front "
                      "of the rim, on the left and right sides, two long rows of shields (垂飾) were hung. These "
                      "consisted of ten hollow golden jade balls connected by a golden ring. At the end, a golden hat "
                      "gourd was suspended. The common decorations of Silla's gold crowns, the stylized and rhomboid "
                      "designs, are similar to those on silver crowns from the Scythai tomb in Novocherkassk, "
                      "South Russia. In Siberian shamanic crowns, deer antlers are actually found in some cases. "
                      "Therefore, it is believed that Silla gold crowns are closely related to ancient northern "
                      "cultures and strongly reflect their shamanistic nature.",
        'king_chair': '',
        'gold_shoes': '',
        'stone_stele': "Bukhansan Bibong, 16th year of King Jinheung of Silla (555) The Pure Monument of King "
                       "Jinheung of Silla on Mount Bukhansan is one of several pure monuments erected by King "
                       "Jinheung (reigned 540-576) as he traveled through his newly acquired territories. It was "
                       "built around 555 on the summit of Bukhansan Bibong in Gugi-dong, Jongno-gu, Seoul, "
                       "Korea. During the Joseon Dynasty, it was known as the Stele of Moohakdasa, but its true "
                       "nature was revealed in 1816 when it was examined by the keumseok scholar Kim Jung-hee ("
                       "1786-1856). On the left side of the monument, Kim's findings are recorded.",
        'stone_sword': '',
        'not_skatch_bowl': '',
        'skatch_bowl': '',
        'old_josun_bronze_sword': '',
        'sun_watch': '',
        'temple_stele': '',
        'cannon': '',
    }

    data = {
        'name': name,
        'image': img,
        'korDes': des,
        'engDes': eng_des[eng_name],
        'youtubeLink' : []
    }

    return data
