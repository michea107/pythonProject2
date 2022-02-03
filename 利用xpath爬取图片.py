from lxml import etree

import requests
import os
import lxml
# 新建文件夹./4kmeinv
if not os.path.exists('./4kmeinv'):
    os.mkdir('./4kmeinv')
# 获取网页文本数据
headers={
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'
}

for n in range(3):
    url = f'https://pic.netbian.com/4kyouxi/index_{n}.html'
    reponse = requests.get(url=url, headers=headers)
    reponse.encoding = 'gbk'
    page_text = reponse.text
    # 对网站文本数据进行xpath解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        imgsrc = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        imgname = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_content=requests.get(url=imgsrc,headers=headers).content
        imgpath = '4kmeinv/'+imgname
        # 持久化储存数据
        with open(imgpath,'wb')as fp:
            fp.write(img_content)
        print(imgname+'下载成功！！！')