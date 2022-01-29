import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Mobile Safari/537.36 '
}
data = {
    'cname':'',
    'pid':'',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '50'
}
response = requests.post(url=url,data=data,headers=headers)
kfc_date=response.json()
filename='kfc.json'

fp = open(filename,'w',encoding='utf-8')
json.dump(kfc_date,fp=fp,ensure_ascii=False,indent=2)
print('over!!')

