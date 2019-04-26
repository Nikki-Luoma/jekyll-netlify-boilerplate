import requests
from bs4 import BeautifulSoup
import numpy

import pandas as pd
import time

page_link = 'https://www.nasdaq.com/symbol/aapl/real-time'

page_resonse = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_resonse.content, "html.parser")

def get_stock_name(soup):
    name = []
    for div in soup.find_all(name="h1", attrs={"class": "qwidget"}):
        for a in div.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return(jobs)
