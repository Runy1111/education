import requests
from bs4 import BeautifulSoup
from time import sleep
from Par_code import get_info, headers


def array():
    for card_url in get_info():

        r = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(r.text, "lxml")
        data = soup.find("div", class_="my-8 w-full rounded border")

        name = data.find('h3').text
        price = data.find('h4').text
        text = data.find('p').text
        url_img = "https://scrapingclub.com" + data.find('img').get('src')

        yield name, price, text, url_img
