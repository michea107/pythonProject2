import requests
import os
import re
if not os.path.exists('./douban'):
    os.mkdir('./douban')
for i in range(11):
    n = i * 25
    url = f'https://movie.douban.com/top250?start={n}&filter='
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Mobile Safari/537.36 '
    }
    page_text = requests.get(url=url, headers=headers).text
    ex = '<li>.*?src="(.*?)"'
    img_src_list = re.findall(ex, page_text, re.S)
    print(img_src_list)
    for src in img_src_list:
       img_date = requests.get(url=src,headers=headers).content
       img_name = src.split('/')[-1]
       imgPath = './douban/'+img_name
       with open(imgPath,'wb') as fp:
           fp.write(img_date)
           print(img_name+'下载成功',i)
print('over')
