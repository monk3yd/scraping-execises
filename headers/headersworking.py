# https://www.youtube.com/watch?v=Oz902cJcCUg
import requests

url = "https://httpbin.org/headers"

response = requests.get(url)
print(response.text)
