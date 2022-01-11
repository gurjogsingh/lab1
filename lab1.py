import requests

print(requests.__version__)

url = "http://google.com/"
print(requests.get(url).status_code)