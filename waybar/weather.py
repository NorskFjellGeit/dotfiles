#!/usr/bin/env python3

import requests

YR_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat=58.33947883&lon=8.5930341&altitude=0"

temp = -99

try:
    data = requests.get(YR_URL, headers={"User-Agent": "Waybar Weather"}, proxies={"https": "http://proxy-wan.tc.nsc.no:3128"})
    data.raise_for_status()
    djson = data.json()
    temp = djson['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
except Exception as e:
    print("ERROR", e)

print(f" {temp}°C")