import requests

print(requests.__version__)

url = "http://google.com/"
print(requests.get(url).status_code)


urlRaw = "https://raw.githubusercontent.com/gurjogsingh/lab1/master/lab1.py"
toPrint = requests.get(urlRaw)
print(toPrint._content)
