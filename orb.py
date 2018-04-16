import requests
import time
import numpy as np

for i in range(3):
    x = requests.get('http://192.168.1.14/api/YwWVvDWK9xetVtmvTPRSnaGBBPfjRwjc3nBvLZTy/lights/5')
    #print(x.text)
    r = requests.put('http://192.168.1.14/api/YwWVvDWK9xetVtmvTPRSnaGBBPfjRwjc3nBvLZTy/lights/5/state',
            data = {'bri':'{}'.format(np.random.randint(0,50)), 'transitiontime':20})
    print(r.text)
    time.sleep(1)

