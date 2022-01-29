import json
import requests
while True:
    answer = input('欢迎进入百度翻译，开始翻译请按1，退出翻译请按0')
    if answer == '1':
        #1.指定url
        post_url = 'https://fanyi.baidu.com/sug'
        #2.进行UA伪装
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.71 Mobile Safari/537.36 '
        }
        #3.post请求参数处理（同get请求一致）
        kw=input('请输入要翻译的单词:')
        data={
            'kw':kw
        }
        #4.发送请求
        response = requests.post(url=post_url,data=data,headers=headers)
        #5.获取相应数据：json（）方法返回的是obj（如果确认响应数据时json类型，才可以使用json（））
        dic_obj=response.json()
        #持久化储存
        filename='baidu.json'
        fp=open(filename,'a',encoding='utf-8',newline='\n')
        json.dump(dic_obj,fp=fp,ensure_ascii=False,indent=2)
        print('over')
    elif answer=='0':
        print('感谢您的使用')
        break
    else:
        print('请输入正确的数字')
        continue
