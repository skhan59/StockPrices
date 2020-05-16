import bs4
import requests as requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


stockInfo = str(raw_input("Enter the stock you want to see:"))

if (stockInfo == "Facebook") | (stockInfo == "FB"):

    def parseFBPrice():
        url = "https://finance.yahoo.com/quote/FB?p=FB"  # Website we're getting stock info from
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
            'span').text  # used 'inspect element' on yahoo to find where the code for the stock info came from
        return price


    while True:  # While true (always) the function will print out the current price of Facebook stock

        print(" The current price of Facebook stock is: $" + str(parseFBPrice()))

        break

elif (stockInfo == "Microsoft") | (stockInfo == "MSFT"):

    def parseMSFTPrice():
        url = "https://finance.yahoo.com/quote/MSFT/"  # Website we're getting stock info from
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
            'span').text  # used 'inspect element' on yahoo to find where the code for the stock info came from
        return price


    while True:  # While true (always) the function will print out the current price of Microsoft stock
        n = 0

        print(" The current price of Microsoft stock is: $" + str(parseMSFTPrice()))

        break


elif (stockInfo == "Amazon") | (stockInfo == "AMZN"):

    def parseAMZNPrice():
        url = "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"  # Website we're getting stock info from
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
            'span').text  # used 'inspect element' on yahoo to find where the code for the stock info came from
        return price


    while True:  # While true (always) the function will print out the current price of Microsoft stock
        n = 0

        print(" The current price of Amazon stock is: $" + str(parseAMZNPrice()))

        break


elif (stockInfo == "Apple") | (stockInfo == "AAPL"):

    def parseAAPLPrice():
        url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"  # Website we're getting stock info from
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
            'span').text  # used 'inspect element' on yahoo to find where the code for the stock info came from
        return price


    while True:  # While true (always) the function will print out the current price of Microsoft stock

        print(" The current price of Apple stock is: $" + str(parseAAPLPrice()))

        break

elif (stockInfo == "Alphabet") | (stockInfo == "GOOG"):

    def parseGOOGPrice():
        url = "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"  # Website we're getting stock info from
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        price = soup.findAll('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
            'span').text  # used 'inspect element' on yahoo to find where the code for the stock info came from
        return price


    while True:  # While true (always) the function will print out the current price of Microsoft stock

        print(" The current price of Alphabet stock is: $" + str(parseGOOGPrice()))

        break
else:
    print("U made a mistake")

