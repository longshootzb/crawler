import requests
import json
proxies ={
    "http":"http://10.10.1.10:3128",
    "https":"https://10.10.1.11:3128"
}
res = requests.get("https://www.sina.com.cn",proxies = proxies)
res.encoding = 'utf-8'
print(res.text)
import urllib.request


