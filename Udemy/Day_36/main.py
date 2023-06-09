STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os
import requests
from twilio.rest import Client

alpha_api_key = "KVD1FFS0GLJRO3MK"
news_api_key = "b5b36c3ee885424e8446b91956e15f41"
params = {
    "stock_param": {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": alpha_api_key
    },
    "news_param": {
        "q": COMPANY_NAME,
        "language": "en",
        "pagesize": 3,
        "apikey": news_api_key
    }
}

## STEP 1: Use https://www.alphavantage.co
stock_price = requests.get(url="https://www.alphavantage.co/query", params=params["stock_param"])
stock_price.raise_for_status()
stock = stock_price.json()["Time Series (Daily)"]
prices = []
for value in stock.values():
    if len(prices) < 2:
        prices.append(float(value["5. adjusted close"]))

diff_percent = round(100 * (prices[0] - prices[1]) / prices[1])

if abs(diff_percent) > 4:
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news = requests.get(url="https://newsapi.org/v2/everything", params=params["news_param"])
    news.raise_for_status()
    articles = news.json()["articles"]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.environ.get("twilio_account_sid")
    auth_token = os.environ.get("twilio_auth_token")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="TESLA: " + ("🔻" if diff_percent < 0 else "🔺") + f"{diff_percent}%\nHeadline: {articles[0]['title']}\nBrief: {articles[0]['description']}",
        from_='+12543584761',
        to='+821098299803'
     )
    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
