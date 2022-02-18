
import requests
from requests.api import request
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=66LE5GJMILPHVE29
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = "66LE5GJMILPHVE29"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "5b29cb0bec3a433fba44faf3f8cb0386"
new_parameters = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,
}

'''Twilio'''
TWILIO_ACCOUNT_SID = 'AC393ae015001a9ac56f251a24bfa4b437'
TWILIO_AUTH_TOKEN = '272340dbc24be6dd073da81b7aed34ca'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

'''Stocks'''
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
'''Closing Price Yesterday'''
closing_price_yesterday = data_list[0]["4. close"]
'''Closing Price Day before Yesterday'''
closing_price_dby = data_list[1]["4. close"]

'''Difference'''
difference = float(closing_price_yesterday) - float(closing_price_dby)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference/float(closing_price_yesterday))*100)

'''Articles'''
if abs(diff_percent) > 1:
    new_response = requests.get(url=NEWS_ENDPOINT,params=new_parameters)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    '''Twilio SMS'''
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+18125944188',
            to='+16262137688'
        )
