# https://www.youtube.com/watch?v=Oz902cJcCUg
import requests

url = "https://httpbin.org/headers"

# Set custom headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept-Language": "en-US;q=0.5",
    "Referer": "https://google.com",
    "DNT": "1"
}

response = requests.get(url, headers=headers)
print(response.text)
