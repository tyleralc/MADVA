from lxml import etree
import sys 
import requests 
from bs4 import BeautifulSoup


def scrap(url):
    website= url
    response=requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

if __name__ == '__main__':
    k=sys.argv[1]
    scrap(k)
