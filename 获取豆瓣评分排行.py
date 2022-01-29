import requests
import json

url='https://movie.douban.com/j/chart/top_list'
"""param = {
    'type':'11',
    'interval_id':'100:90',
    'action':"" ,
    'start':'0',
    'limit':'100',
}"""
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Mobile Safari/537.36 '
}
respone=requests.get(url=url,params=param,headers=headers)
data = respone.json()
fp=open('douban.json','w',encoding='utf-8')
json.dump(data,fp=fp,ensure_ascii=False,indent=1)
print('over')
