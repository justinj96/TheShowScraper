import requests
import threading
from message import sendMessage 
import datetime

def priceAlert():
    
    timeInterval = 600.0

    threading.Timer(timeInterval, priceAlert).start()
    print(f'Price checked at {datetime.datetime.now()}')
    
    response = requests.get(f"https://theshownation.com/mlb20/apis/listings.json?type=mlb_card&page=6").json()
    
    for item in response['listings']:
        if item.get('name') == 'Aroldis Chapman':
            if item.get('best_sell_price') > 185000:
                message = "Aroldis Price Reached"
                sendMessage(message)
            break

priceAlert()