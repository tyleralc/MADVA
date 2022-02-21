from lxml import etree
import sys 
import requests 
from bs4 import BeautifulSoup
import pandas as pd


def scrap_courses(url):
    html = pd.read_html(url, header = 0)
    df = html[0]
    print(df)
    return df 
if __name__ == '__main__':
    k=sys.argv[1]
    scrap(k)

