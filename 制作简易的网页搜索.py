import requests
""""	
UA：user-agent（请求载体的身份标识）
UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，说明请求是一个正常的请求。但是如果检测道德请求的
是放在载体身份标识不是基于某一款浏览器的，则表示该请求为不正常请求（爬虫），则服务器很有可能拒绝该次请求。
UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
"""
url = 'https://www.sogou.com/web?'
# UA伪装：将对应的User-Agent封装到一个字典中
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Mobile Safari/537.36 '
}
# 处理url携带的参数：封装到字典中
kw = input('请输入关键词：')
param = {'query': kw}
# 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
filename = kw + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('保存成功')
