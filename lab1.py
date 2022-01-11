import requests

print(requests.__version__)

url = "http://google.com/"
print(requests.get(url).status_code)

urlRaw = "https://raw.githubusercontent.com/gurjogsingh/lab1/87907753781e726d3987cf0ab5ccaae1fb10c04f/lab1.py?token=GHSAT0AAAAAABQOMSLGR6YZJBJUI7KJOJT4YO46M3Q"
