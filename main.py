#get the url from amazon
#get the availability--if the product come In stock---notify via gmail
#In mail I need Link-Instock
#automatically per hour
import time

import requests
from bs4 import BeautifulSoup
import smtplib

def check_avail():
    url = 'https://www.amazon.in/Smart-AMOLED-Display-Battery-Resistant/dp/B08TBKJ5LZ/ref=sr_1_1?keywords=mi%2Bfit%2Bband%2B5&qid=1637503034&qsid=257-8246201-5785306&sr=8-1&sres=B08GXC2NTX%2CB08KQLK2RC%2CB09J2C7YDH%2CB08GMP6VRS%2CB09G6QV45F%2CB09FYZGB5T%2CB09GP8QZZQ%2CB09F2HHDFT%2CB09HC7KQNQ%2CB09J4WVQ8C%2CB09FFKH5Y2%2CB09FPYY7B2%2CB091G3FLL7%2CB09LR1HWR6%2CB09KQ77S9Y%2CB07XY9BZPM%2CB08W49129G%2CB08R91SZSN%2CB09FD6ZYTD%2CB09FF1PLFM&srpt=WEARABLE_COMPUTER&th=1'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Cache-Control': 'no-cache', "Pragma": "no-cache"}
    # send a http request
    page = requests.get(url, headers=header)
    content = BeautifulSoup(page.content, 'html.parser')
    # checking availability status
    availability = content.find(id="availability").get_text().strip().replace("\n", "")
    #print(availability)
    # check availibility---if Instock ----send gmail

    if(availability=='In stock.'):
        send_mail()



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bhagya.workacc@gmail.com','jgjeqamrkcndebdn')

    subject = 'Product is now available in stock'
    body    = 'Click the link https://www.amazon.in/Smart-AMOLED-Display-Battery-Resistant/dp/B08TBKJ5LZ/ref=sr_1_1?keywords=mi%2Bfit%2Bband%2B5&qid=1637503034&qsid=257-8246201-5785306&sr=8-1&sres=B08GXC2NTX%2CB08KQLK2RC%2CB09J2C7YDH%2CB08GMP6VRS%2CB09G6QV45F%2CB09FYZGB5T%2CB09GP8QZZQ%2CB09F2HHDFT%2CB09HC7KQNQ%2CB09J4WVQ8C%2CB09FFKH5Y2%2CB09FPYY7B2%2CB091G3FLL7%2CB09LR1HWR6%2CB09KQ77S9Y%2CB07XY9BZPM%2CB08W49129G%2CB08R91SZSN%2CB09FD6ZYTD%2CB09FF1PLFM&srpt=WEARABLE_COMPUTER&th=1 '
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('bhagya.workacc@gmail.com','bhagya.workacc@gmail.com',msg)

    server.quit()


while(True):
    check_avail()
    time.sleep(3600)
