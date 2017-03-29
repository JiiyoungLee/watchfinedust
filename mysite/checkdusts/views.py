#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from bs4 import BeautifulSoup
import requests
from datetime import *
import json

from . models import LocationInfo, DustInfo

# Create your views here.
def index(request):
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
        except ValueError:
            #pass
            myDict['name'] = item['city']
        finally:
            myDict['dust'] = item['aqi']
            mySet.append(myDict)
    return render(request, 'checkdusts/index.html', {'mySet' : mySet})
"""	mySet = [];
	dustInfoSet = [];


	for i in range(LocationInfo.objects.count()):
		loc_info = LocationInfo.objects.get(pk=i+1).getLocationInfo()
		mySet.append(loc_info)
	for i in range(LocationInfo.objects.count()):
		dust_info = DustInfo.objects.get(pk=i+1).getDustInfo()
		mySet.append(dust_info)
	return render(request, 'checkdusts/index.html', {'name' : mySet.name, 'dust' : mySet, 'loc_count': LocationInfo.objects.count() })
"""
def detail(request, location_id):
	try:
		location = LocationInfo.objects.get(pk=location_id)
		dust = DustInfo.objects.get(name=location)
	except LocationInfo.DoesNotExist:
		raise Http404("That location_id does not exist")
	#response = "you input %s as location_id."
	#return HttpResponse(response % location_id)
	return render(request, 'checkdusts/detail.html', {'location' : location, 'dust' : dust})

#def crawling(requset):
   
"""
def crawling(request):
	return render(request, 'checkdusts/crawling.py')

def crawl_finedust(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    resultSet = []
    dustSet = []
    dataDict = dict({'location' : "" , 'dust' : []})
    dataSet = soup.find_all('td')
    for data in dataSet:
        data = str(data.get_text())
        if len(data) != 0:
            if data[0] == '[':
                resultSet.append(data)
            elif data == '도시대기':
                pass
            elif data == '도로변대기':
                pass
            elif data == '교외대기':
                pass
            elif data == '-':
                pass
            elif data == '국가배경농도':
                pass
            elif int(data):
                resultSet.append(data)
    return resultSet


def crawling_test(request):
    if request.method == "GET":
        mySet = []
        myDict = {}
        main_url = 'http://www.airkorea.or.kr/pmRelaySub'
        today = str(date.today())
        print(today)
        mySet.append(crawl_finedust(main_url+'?strDateDiv=1&searchDate='+today+'&district=02&itemCode=10007&searchDate_f=201703'))
        print(mySet)
        for i in range(len(mySet[0])):
            if i == 0:
                myDict['location'] = mySet[0][0]
            elif i == len(mySet[0]) - 1:
                myDict['recent_dust'] = mySet[0][i]
                resultSet.append(myDict)
            else :
                if mySet[0][i][0] == '[':
                    myDict['recent_dust'] = mySet[0][i - 1]
                    resultSet.append(myDict)
                    myDict['location'] = mySet[0][i]  
        return HttpResponse(myDict)
"""
