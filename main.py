import sys
sys.path.insert(0, 'lib')
import requests
from flask import Flask, redirect, url_for, request, render_template
import json
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
   sum = 0

   for ticker in response["quoteResponse"]["result"]:
      sum += ticker["regularMarketPrice"]
      mPrice = ticker["regularMarketPrice"]
      if ticker["symbol"] == "AMC":
         amcPrice = f"AMC \n{mPrice}"
      if ticker["symbol"] == "APE":
         apePrice = f"APE \n{mPrice}"

      allTickers.append(ticker["regularMarketPrice"])

   print(amcPrice)
   print(apePrice)
   print(sum)
   return render_template("index.html", data="{:.2f}.format(sum)", amc=amcPrice, ape=apePrice)
