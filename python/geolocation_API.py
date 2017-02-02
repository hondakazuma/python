# -*- coding: utf-8 -*-

import urllib
import json
import requests

URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
KEY = "AIzaSyDQLxXccBuzaWU4OiMEvqzFCxUrEValckw"
HEADER = {"Content-Type": "application/json"}

def get_gps_from_geolocation_api():

    url = URL
    key = KEY
    header = HEADER

    params = {
      "wifiAccessPoints": [
        {
            "macAddress": "00:25:9c:cf:1c:ac",
            "signalStrength": -43,
            "signalToNoiseRatio": 0
        },
        {
            "macAddress": "00:25:9c:cf:1c:ad",
            "signalStrength": -55,
            "signalToNoiseRatio": 0
        }
      ],
      "headers": header
    }

    # request = (url, params, header)
    # paramsをjson形式に変換
    json_par = json.dumps(params)

    #request文作成
    req_to = url + key
    print(req_to)

    # request送信
    res = requests.post(req_to, json_par)

    # response取得
    print(res)
    response = res.json()
    print(response)

    

get_gps_from_geolocation_api()
