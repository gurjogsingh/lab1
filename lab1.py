import requests

print(requests.__version__)

url = "http://google.com/"
print(requests.get(url).status_code)

urlRaw = "https://raw.github.com/django/django/master/setup.py"
toPrint = requests.get(urlRaw)
print(toPrint._content)
