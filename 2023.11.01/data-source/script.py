# Import necessary packages
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import csv

url = "https://www.ncstatefair.org/2023/Newsroom/attendance.htm"
html_name = "fair_raw.html"
data_name = "fair_clean.csv"

# html = requests.get(url)
# file = open(html_name, 'wb')
# file.write(html.content)
# file.close()

with open(html_name) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(type(soup))