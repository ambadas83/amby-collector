import requests
from bs4 import BeautifulSoup

url = "https://www.lovethework.com/en/awards/winners-shortlists/cannes-lions/audio-radio?tag=publication+dates%40%40year%40%402026"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text,"html.parser")

print(soup.title.text)
