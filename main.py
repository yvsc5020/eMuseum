import numpy as np
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
import cv2


app = FastAPI()


def getData(dataList):
    liList = driver.find_element(By.XPATH, "//*[@id='container']/div[2]/ul[2]").find_elements(By.TAG_NAME, "li")

    for item in liList:
        dataDict = {'poster': item.find_element(By.TAG_NAME, "img").get_attribute("src"),
                    'title': item.find_element(By.CLASS_NAME, "name").text,
                    'date': item.find_element(By.CLASS_NAME, "date").text,
                    'place': item.find_element(By.CLASS_NAME, "place").text,
                    'genre': item.find_element(By.CLASS_NAME, "genre ").text,
                    'time': item.find_element(By.CLASS_NAME, "time ").text,
                    'price': item.find_element(By.CLASS_NAME, "price").text}

        dataList.append(dataDict)


options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                     "like Gecko) Chrome/77.0.3865.75 ""Safari/537.36")
options.add_argument('--headless')
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
                                                    'geolocation': 2, 'notifications': 2,
                                                    'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2,
                                                    'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2,
                                                    'media_stream_camera': 2, 'protocol_handlers': 2,
                                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                    'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                    'metro_switch_to_desktop': 2, 'protected_media_identifier': 2,
                                                    'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)


@app.get("/theater")
def theater():
    url = "https://www.ntok.go.kr/kr/Ticket/Performance/Index"
    driver.get(url)

    driver.find_element(By.XPATH, "//*[@id='container']/div[2]/div[1]/fieldset/div[1]/ul/li[4]/a").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='container']/div[2]/ul[2]/li[2]")))

    dataList = []

    getData(dataList)

    aList = driver.find_element(By.XPATH, "//*[@id='container']/div[2]/div[3]/div").find_elements(By.TAG_NAME, "a")
    for a in aList:
        a.click()
        time.sleep(0.5)

        getData(dataList)

    return dataList
