# import urllib.request
# res = urllib.request.urlopen('http://www.baidu.com')
# print(res.read().decode('utf-8'))

import requests
import json
res = requests.get("https://httpbin.org/get")
print(type(res))
print(res.status_code)
print(type(res.text))
print(res.text)
# print(res.cookies)
# print(res.json)
print(json.loads(res.text))