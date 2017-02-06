# -*- coding: utf-8 -*-

import pandas as pd
import urllib
import json
import requests

URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
KEY = "AIzaSyDQLxXccBuzaWU4OiMEvqzFCxUrEValckw"
HEADER = {"Content-Type": "application/json"}

# APIに投げる情報を持っているファイル
INFO_DIR = "/Users/hondakazuma/python/samplefile/sample_csv/"
INFO_FILE = "wifi_cell_info.csv"

def get_gps_from_geolocation_api():

    url = URL
    key = KEY
    header = HEADER

    # APIに投げる情報を持っているファイルの読み込み
    to_API = pd.read_csv(INFO_DIR + INFO_FILE)

    for i in range(0, len(to_API.index)):

        wifi_info = to_API.ix[i, 'wifi_info']
        cell_info = to_API.ix[i, 'cell_info']

        params = {
        "wifiAccessPoints": [
            {
                "macAddress": wifi_info,
            }
        ],
        "cellTowers": [
            {
                "cellId": cell_info,
                "locationAreaCode": 4288,
                "mobileCountryCode": 440,
                "mobileNetworkCode": 10,
            }
        ],
          "headers": header
        }

        # request = (url, params, header)
        # paramsをjson形式に変換
        json_par = json.dumps(params)

        #request文作成
        req_to = url + key

        # request送信
        res = requests.post(req_to, json_par)

        # response取得
        response = res.json()

        # dataframeに格納
        # DataFrame({'列名1:[行の値1,行の値2,…]','列名2:[行の値1,行の値2,…]'… })
        gps_from_API = pd.DataFrame({'lat': [], 'lng': [], 'accuracy': []})

        # APIから取得した値の代入
        gps_from_API.ix[i, 'accuracy'] = response['accuracy']
        gps_from_API.ix[i, 'lng'] = response['location']['lng']
        gps_from_API.ix[i, 'lat'] = response['location']['lat']
        print(gps_from_API)



get_gps_from_geolocation_api()
