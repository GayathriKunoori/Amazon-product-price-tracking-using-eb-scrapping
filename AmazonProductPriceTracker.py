import requests               #it will help us to get our url directed
from bs4 import BeautifulSoup         #it will help us to scrap the data

import os
import smtplib                 #this is a module used for sending emails
from email.message import EmailMessage

import time

email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")

URL="https://www.amazon.in/dp/B07H9T3MD1/ref=va_live_carousel?pf_rd_r=ZZSTK40EQ9M1ME3VJA2K&pf_rd_p=36443c07-831c-4bcd-8c9a-ccdff23bf7aa&pf_rd_m=A21TJRUUN4KGV&pf_rd_t=Gateway&pf_rd_i=desktop&pf_rd_s=desktop-3&pd_rd_i=B07H9T3MD1&th=1&psc=1"
#copy the url of the product which you are looking for

def check_price():

    headers={"user-Agents" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    page = requests.get(URL , headers=headers)
    soup = BeautifulSoup(page.content , 'html.parser')

    #let's print our product title 
    title = soup.find(class_ ="a-size-large a-spacing-none").get_text()
    price = soup.find(class_ ="a-price-whole").get_text()
    converted_price= int(price[0:8].replace(",",""))  #Ignoring numbers after decimal point
    print("PRODUCT DETAILS:")
    print(title.strip())    #strip() is used to avoid the spaces
    print("Price:",converted_price)
    print("-71 {0} off".format("%"))
    print("Package Dimensions: 14 x 8 x 6 cm; 70 Grams")
    print("Date First Available : 6 January 2020")
    print("ASIN  :  B083KB3Z59")
    print("Item part number  :  DE599")
    print("Country of Origin  :  India")
    print("Department :  Unisex")
    print("Item Weight : 70 g")
    print("Best Sellers Rank: #219,217 in Clothing & Accessories ")
    #It will send the mail if the price is decreased than present price
    if(converted_price < 579):
       send_mail()

#function for sending mail

def send_mail():
    msg = EmailMessage()
    msg['Subject'] = "Product price fell down"
    msg['From'] = email_id
    msg['To'] = "kunoorigayathri@gmail.com"
    msg.set_content("Hey check this amazon link :https://www.amazon.in/dp/B07H9T3MD1/ref=va_live_carousel?pf_rd_r=ZZSTK40EQ9M1ME3VJA2K&pf_rd_p=36443c07-831c-4bcd-8c9a-ccdff23bf7aa&pf_rd_m=A21TJRUUN4KGV&pf_rd_t=Gateway&pf_rd_i=desktop&pf_rd_s=desktop-3&pd_rd_i=B07H9T3MD1&th=1&psc=1")

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:    #587 is the port number
        smtp.login(email_id,email_pass)
        smtp.send_message(msg)


while True:
    check_price()
    time.sleep(10)

        

