#scrapping IPL website and getting data of sold players in 2023 and by pandas converting them into comma seperated values

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
#l =soup.prettify()
#print(l)




taable = soup.find_all("table", id="t1")
#print(taable)

# this data set contains many table element



l1 = []
for i in taable:
       heading = i.thead.get_text().strip('\n').split("\n")

       l1.append(heading)

#print(l1[0])

#df = pd.DataFrame(columns = l1[0])



#now getting data
dtt = []
for j in taable:
   data = j.find_all("td")
   for k in data:
      datas = k.get_text()
      dtt.append(datas)

#print(dtt)

nl = []

for a in range(0,len(dtt),4):
    nl.append(dtt[a:a+4])

print(nl)

df = pd.DataFrame(data=nl , columns=l1[0])
print(df)
df.to_csv("sold players in IPL 2023.CSV")