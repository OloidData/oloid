import requests
import time
import math

#x = requests.get('http://192.168.1.14/api/YwWVvDWK9xetVtmvTPRSnaGBBPfjRwjc3nBvLZTy/lights/5')
#print(x.text)

while True:
    for i in range(30):
        value = i/30 * math.pi
        print("value", value)
        brightness = math.floor(math.sin(value) * 250) + 4
        print("brightness", brightness)
        r = requests.put('http://192.168.1.14/api/YwWVvDWK9xetVtmvTPRSnaGBBPfjRwjc3nBvLZTy/lights/5/state',
                json = {'bri':brightness, 'transitiontime':3})
        time.sleep(0.3)
    time.sleep(0.35)

