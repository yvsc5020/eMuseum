from PIL import Image
import tensorflow as tf
import numpy as np
import io


def getResult(file):
    img = Image.open(io.BytesIO(file))
    img_resize = img.resize((300, 300))

    img_array = tf.keras.utils.img_to_array(img_resize)
    img_array = tf.expand_dims(img_array, 0)

    model = tf.keras.models.load_model('domain/image/models/eMuseum.h5')

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ['big_map', 'bronze_mirror', 'check_rain', 'fist_axe',
                   'gold_crown', 'king_chair', 'not_skatch_bowl',
                   'old_josun_bronze_sword', 'skatch_bowl', 'stone_sword',
                   'sun_watch', 'temple_stele', 'ten_stonetower', 'thin_bronze_sword']
    result = {
        'bronze_mirror': '청동거울',
        'check_rain': '측우기',
        'ten_stonetower': '경천사 십층석탑',
        'gold_crown': '금관',
        'king_chair': '근정전 어좌',
        'bronze_ware': '농경문 청동기',
        'big_map': '대동여지도',
        'stone_sword': '돌칼',
        'not_skatch_bowl': '민무늬토기',
        'skatch_bowl': '빗살무늬토기',
        'old_josun_bronze_sword': '고조선 청동검',
        'sun_watch': '앙부일구',
        'temple_stele': '원랑선사_탑비',
        'fist_axe': '주먹도끼',
        'thin_bronze_sword': '세형동검'
    }
    eng_name = class_names[np.argmax(score)]

    return result[eng_name]
