import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import smtplib, ssl

# Price you are after
BUY_PRICE = 500

# Get EMAIL details from .env file
load_dotenv()
SMTP_ADDRESS=os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS")

# Enter the URL in this format of the Amazon item that you're looking for
URL="https://www.amazon.com/HP-Desktop-Display-Processor-Keyboard/dp/B0B6523VBD/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, features="lxml")

# Get the price and title using BeautifulSoup
price_tag = soup.find("span", class_= "a-offscreen").getText()
price = price_tag[1:]
title = soup.find(id="productTitle").get_text().strip()

#Send email
if float(price) < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=TO_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )


