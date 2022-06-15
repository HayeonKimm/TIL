import requests
import json
import xmltodict
import json
import requests
from bs4 import BeautifulSoup
import time
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.b7vsn.mongodb.net/?retryWrites=true&w=majority')
db = client.test

url = 'http://data.ex.co.kr/openapi/restinfo/restBestfoodList'
KEY = '********'
TYPE = 'json'
NUMOFROWS = 99

# response = requests.get(url)
# print(response.status_code)
# print(response.text)


# http://data.ex.co.kr/openapi/restinfo/restBestfoodList?key=test&type=xml&numOfRows=10&pageNo=1


for pageNo in range(1,99):
    KEY = '3217743800'
    requestUrl = 'http://data.ex.co.kr/openapi/restinfo/restBestfoodList?key={}&type=json&numOfRows=99&pageNo={}'.format(KEY,pageNo)
    res = requests.get(requestUrl)
    text = res.text
    data= json.loads(text)


    if data['list'][0] is not None:

        a,b,c,d,e,f= data['list'][0]['stdRestNm'], data['list'][0]['foodNm'], data['list'][0]['stdRestNm'],data['list'][0]['svarAddr'],data['list'][0]['foodCost'],data['list'][0]['routeNm']

        doc = {
            'stdRestNm': a,
            'foodNm': b,
            'stdRestNm':c,
            'svarAddr':d,
            'foodCost':e,
            'routeNm':f
        }
        db.high.insert_one(doc)












