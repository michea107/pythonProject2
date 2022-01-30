import requests
import bs4
import lxml
from bs4 import BeautifulSoup
import os
#使用bs4爬取妹子图
if not os.path.exists('./meizi'):
    os.mkdir('./meizi')
#对首页面数据进行爬取
url = 'https://www.jdlingyu.com/tuji'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Mobile Safari/537.36 '
}
page_text = requests.get(url=url,headers=headers).text
#在首页面中解析出详情页的url
soup = bs4.BeautifulSoup(page_text, 'lxml')
a_list=soup.select('.post-module-thumb')

for li in a_list:
    content_url=li.a['href']
    print(content_url)
    content_text=requests.get(url=content_url,headers=headers).text
    content_soup=bs4.BeautifulSoup(content_text,'lxml')
    scr_list=content_soup.select('.entry-content>img')
    i=0
    #获取详情页图片的url
    for scr in scr_list:
        i=i+1
        img_url=scr['src']
        img_content=requests.get(url=img_url,headers=headers).content
        img_name = img_url.split('/')[-1]
        img_path = './meizi/'+img_name
        #导出图片的url
        with open(img_path,'wb')as fp:
            fp.write(img_content)
            print(img_name+'下载成功',i)
