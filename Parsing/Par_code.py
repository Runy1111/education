import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}


def get_info(url):
    sleep(3)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    data = soup.find_all("div", class_="w-full rounded border")

    for now in data:
        name = now.find('h4').text.replace('\n', '')
        price = now.find('h5').text
        source = "https://scrapingclub.com" + now.find('img', class_='card-img-top img-fluid').get('src')
        print(name + '\n' + price + '\n' + source + '\n\n')



