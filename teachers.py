import requests 
import pandas as pd
from bs4 import BeautifulSoup



def main():
    page= requests.get('https://catalogue.usc.edu/content.php?catoid=14&navoid=5199')
    soup = BeautifulSoup(page.content, 'html.parser')
    #fac=soup.find(class_="block_content .table_default").get_text()
    fac = soup.select(".block_content .table_content")
    periods = [f.get_text() for f in fac]
    # for f in fac:
    #     f.get_text()
    print(periods)



if __name__ == '__main__':
    main()