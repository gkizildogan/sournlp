import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import csv
import pandas as pd

url = "https://eksisozluk.com/gibi-dizi--6838897?p="
entries = []
for page_num in range(1, 1065):
    time.sleep(1)
    page_req = requests.get(url+str(page_num), headers={"User-Agent": "Chrome"}, timeout=3)
    soup = BeautifulSoup(page_req.content, features="html.parser")
    contents_in_a_page = soup.find_all("div", {"class": "content"})
    entries_in_a_page = [entry.text.strip().replace("--- spoiler ---", " ") for entry in contents_in_a_page]
    df = pd.DataFrame({"Entries": entries_in_a_page})
    if page_num == 1:
        df.to_csv("entries.csv", index=False, quoting=2)
    else:
        df.to_csv("entries.csv", mode="a", index=False, header=False, quoting=2)
