import sys
sys.path.insert(0, 'lib')
import requests
from flask import Flask, redirect, url_for, request, render_template
import json
from currency_converter import CurrencyConverter
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():

   url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=APE,AMC"

   headers = {
      "Accept": "application/json",
      "User-Agent": "",
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
   )

   response = response.json()

   allTickers = []
   pAllTickers = []
   sumReg = 0
   pSum = 0

   for ticker in response["quoteResponse"]["result"]:
      sumReg += ticker["regularMarketPrice"]
      mPrice = ticker["regularMarketPrice"]
      if ticker["symbol"] == "AMC":
         amcPrice = f"AMC \n{mPrice}"
      if ticker["symbol"] == "APE":
         apePrice = f"APE \n{mPrice}"

      allTickers.append(ticker["regularMarketPrice"])

   for pTicker in response["quoteResponse"]["result"]:
      pSum += pTicker["postMarketPrice"]
      pPrice = pTicker["postMarketPrice"]
      if pTicker["symbol"] == "AMC":
         pAmcPrice = f"AMC \n{pPrice}"
      if pTicker["symbol"] == "APE":
         pApePrice = f"APE \n{pPrice}"

      pAllTickers.append(pTicker["postMarketPrice"])

   print(f"Regular market price: {amcPrice}")
   print(f"Regular market price: {apePrice}")
   print(f"Post market price:  {pAmcPrice}")
   print(f"Post market price: {pApePrice}")
   print(f"Regular market sum: {sumReg}")
   print(f"Post market sum: {pSum}")

   return render_template("index.html", data="{:.3f}".format(sumReg), amc=f"Regular market price: {amcPrice} $", ape=f"Regular market price: {apePrice} $", p_data="{:.3f}".format(pSum), p_amc=f"Post market price:{pAmcPrice} $", p_ape=f"Post market price:{pApePrice} $")

app.run()