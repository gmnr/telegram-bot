#!/usr/bin/python3

# crypto.py - the module allows access to the market data available on coinmarketcap.com


import json
import requests
from datetime import datetime


def pretty_print(name, *args):
    pass



def get_response(num_result=5, curr="EUR"):
    """Fetch the data to feed to the bot with the latest listings for cryptos on coinmarketcap.com"""

    # the message that will be sent by the bot
    coin_message = ""

    api_url = f"https://api.coinmarketcap.com/v1/ticker/?convert={curr}&limit={num_result}"

    date = datetime.now().strftime("%d-%m-%y at %H:%M")
    coin_message += f'Data fetched from *coinmarketcap.com* on {date}\n'    # edit format

    res = requests.get(api_url)
    if res.ok:
        price_data = json.loads(res.content)
    else:
        res.raise_for_status()

    # parse the json for data
    for coin in price_data:
        round_price = str(round(float(coin['price_eur']), 3))
        coin_message += "*{}*: {} --> {}%\n".format(coin['symbol'], round_price, coin['percent_change_7d'])

    return coin_message

print(get_response())
