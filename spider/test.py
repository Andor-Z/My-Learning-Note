import requests

r = requests.get('https://github.com', verify=True)
print(r.text)