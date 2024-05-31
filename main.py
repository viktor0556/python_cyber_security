# https://en.wikipedia.org/wiki/Programmer  

import requests

from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html')

get_page(input("What url would you like to scrape? "))