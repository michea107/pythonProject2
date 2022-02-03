import requests
url = 'https://www.baidu.com/s?wd=ip'
# UA伪装：将对应的User-Agent封装到一个字典中
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrom/97.0.4692.71 Mobile Safari/537.36 '
}

response = requests.get(url=url, headers=headers,proxies={})
page_text = response.text
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('保存成功')
response.status_codee