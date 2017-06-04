import json
import requests
res = requests.get("https://github.com/favicon.ico")
with open("favicon.ico","wb") as f:
    f.write(res.content)
    f.close()