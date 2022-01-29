import requests
import json

url='https://www.bilibili.com/video/BV1Yh411o7Sz?p=22&t=479.4'
response_png=requests.get(url=url).content
fp=open('tupian.mp4','wb')
fp.write(response_png)
fp.close()
print('over!!')
