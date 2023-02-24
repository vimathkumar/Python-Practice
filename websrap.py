import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_497d0d76-5ff0-4613-a801-02f748244abb_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=l7xdysrdb40000001675786520539")
# print(response)

soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

names = soup.find_all('div',class_="_4rR01T")
# print(names)
name = []
for i in names[0:20]:
    d = i.get_text()
    name.append(d)
# print(name)

prices = soup.find_all('div',class_="_30jeq3 _1_WHN1")
price = []
for i in prices[0:20]:
    d = i.get_text()
    d1 = d[1:]
    l=[]
    if ',' in d1:
        for i in d1:
            if i==',':
                pass
            else:
                l.append(i)
    # print(''.join(l))
    price.append(float(''.join(l)))
# print(price)

ratings = soup.find_all('div',class_="_3LWZlK")
rate = []
for i in ratings[0:20]:
    d = i.get_text()
    rate.append(float(d))
# print(rate)
images = soup.find_all('img',class_='_396cs4')
image = []
for i in images[0:20]:
    d = i['src']
    image.append(d)
# print(image)
links = soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d = "https://www.flipkart.com"+i['href']
    link.append(d)
# print(link)


df = pd.DataFrame()
df["Names"] = name
df["Prices"] = price
df["Ratings"] = rate
df["Images"] = image
df["links"] = link
print(df)
df.to_csv("Mobiles.csv")