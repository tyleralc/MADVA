import requests 
import pandas as pd
from bs4 import BeautifulSoup
import re


def main():
    page= requests.get('https://catalogue.usc.edu/content.php?catoid=14&navoid=5199')
    soup = BeautifulSoup(page.content, 'html.parser')
    tbody= soup.tbody
    for i in tbody:
        print(i.get_text())

    # text = [f.get_text() for f in p_tags]
    
  


if __name__ == '__main__':
    main()