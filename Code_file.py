import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://ticker.finology.in/"

r=requests.get(url)

print(r)

soup=BeautifulSoup(r.text, "lxml")

#print(soup)

table = soup.find("table", class_="table table-sm table-hover screenertable")

header=table.find_all(("th"))
#print(header)

header_list=[]
for i in header:
    titles = i.text
    header_list.append(titles)

##print(header_list)

df = pd.DataFrame(columns=header_list)
##print(df)

rows=table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    #print(data)
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l]= row

print(df)

df.to_csv(("STOCK MARKET DATA.csv"))




