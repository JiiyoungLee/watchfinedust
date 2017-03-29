import requests
from bs4 import BeautifulSoup
from datetime import *
import json


main_url = 'https://wind.waqi.info/mapq/bounds/?bounds=34.70097741472011,125.16723632812499,38.190704293996504,130.946044921875&inc=placeholders&k=_2Y2EzVBxYM10fIysKSxRWXmldaA0/LRkbFngrLg==&_=1490598978236'
mySet = []
myDict = {}
resultSet = []
page = requests.get(main_url)
i=0
for item in page.json():
    myDict = {}
    try:
        myDict['latitude'] = item['lat']
        myDict['longitude'] = item['lon']
        myDict['name'] = item['city'][item['city'].index('(대한민국')+5:len(item['city']) - 1]
        myDict['dust'] = item['aqi']
        mySet.append(myDict)
    except ValueError:
        myDict['name'] = item['city']
        myDict['dust'] = item['aqi']
        mySet.append(myDict)
print(mySet)
print(len(mySet))

