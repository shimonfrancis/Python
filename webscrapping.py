import pandas as pd
import requests
import smtplib
import time
import datetime
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
url='https://www.amazon.in/ASUS-Zenbook-Flip-OLED-35-56/dp/B0B7B456Q9/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=9vfJD&content-id=amzn1.sym.7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_p=7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_r=C5PFTM5VZ43MB4V0JFC3&pd_rd_wg=4ONqY&pd_rd_r=3f162a57-18ac-453c-a4fe-a26d95f553fd&pd_rd_i=B0B7B456Q9'
page=requests.get(url,headers=headers)
soup1=BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
heading=soup2.find(id='productTitle').get_text()
price=soup2.find(id="mbc-price-1").get_text()
price=price.strip()[1:]
heading=heading.strip()
print(heading)
print(price)
date=datetime.date.today()
import csv
head=['heading','price','date']
data=[heading,price,date]
with open('C:/Users/shimo/Downloads/Softwares/scraper.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(head)
    writer.writerow(data)
def check_price():
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    url='https://www.amazon.in/ASUS-Zenbook-Flip-OLED-35-56/dp/B0B7B456Q9/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=9vfJD&content-id=amzn1.sym.7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_p=7938e11a-362b-421f-bd30-8dd8d3c4b65f&pf_rd_r=C5PFTM5VZ43MB4V0JFC3&pd_rd_wg=4ONqY&pd_rd_r=3f162a57-18ac-453c-a4fe-a26d95f553fd&pd_rd_i=B0B7B456Q9'
    page=requests.get(url,headers=headers)
    soup1=BeautifulSoup(page.content,"html.parser")
    soup2=BeautifulSoup(soup1.prettify(),"html.parser")
    heading=soup2.find(id='productTitle').get_text()
    price=soup2.find(id="mbc-price-1").get_text()
    price=price.strip()[1:]
    heading=heading.strip()
    print(heading)
    print(price)
    date=datetime.date.today()
    head=['heading','price','date']
    data=[heading,price,date]
    with open('C:/Users/shimo/Downloads/Softwares/scraper.csv','w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(head)
        writer.writerow(data)
