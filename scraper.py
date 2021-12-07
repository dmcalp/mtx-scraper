import requests
from bs4 import BeautifulSoup

URL = "https://www.pathofexile.com/shop/category/daily-deals"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

names = soup.find_all('a', {"class": "name"})
prices = soup.find_all('div', {"class": "price"})


print("============ Todays deals ============", '\n')

for name, price in zip(names, prices):
    print(name.text, price.text)

print('\n', URL)
