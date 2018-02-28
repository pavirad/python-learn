
from bs4 import BeautifulSoup

import urllib
import time
import wikipedia
import requests
import numpy

import pandas as pd

def load_data():
    start_time = time.time()
    page = requests.get("https://en.wikipedia.org/wiki/Kurt_Cobain")
    soup = BeautifulSoup(page.content, 'html.parser')

    attribs = (["divorce","depression","drug","book","gambling","mental","medicine","introvert","social","sexual",
                "alcohol","psychosocial","fame","illness","treatment","depressed","marriage","disorder","overdose",
                "abuse","smoking"])

    celeb_row = 0
    flag_found = 0
    celeb = numpy.zeros((1000, len(attribs)))
    cols = pd.Index(attribs)

    df = pd.DataFrame(data = celeb, columns =cols)

    print("----Half time is %s-----", time.time() - start_time)
    half_time = time.time()

    #indices- Divorced is 1,
    #/Assumption divorce keyword found and not necessarily parents
    for html in soup.find_all("p"):
        data = (html.get_text())
        for item in data.split("."):
            for i in range(0, len(attribs)):
                if df.columns[i] in item:
                    celeb[celeb_row, df.columns.get_loc(df.columns[i])] += 1


    print("----Total time is %s-----", time.time() - half_time)
    return df


df_celeb = load_data()
df_celeb.head()

df_celeb.info()

df_celeb.describe()

page1 = requests.get("https://en.wikipedia.org/wiki/Lists_of_celebrities")
soup1 = BeautifulSoup(page1.content, 'html.parser')
for ultag in soup1.find_all('ul', class_='mw-headline'):
    for litag in ultag.find_all('li'):
        a1 = litag.find('a')
        print(a1['href'])
        if a1['href'].startswith("/wiki/"):
            page2 = requests.get("https://en.wikipedia.org"+a1['href'])
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            print(a1['href'])

            for ultag1 in soup2.find_all('ul'):
                for litag1 in ultag1.find_all('li'):
                    print(litag1.text)
