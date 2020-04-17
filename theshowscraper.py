from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import webbrowser
import sys

if len(sys.argv) < 3:
    print(f"Missing Command Line Args")
    print(f"Usage: python3 theshowscraper.py <rarity> <page number>")
    print(f"Rarity: Common = 1, Bronze = 2, etc")
    sys.exit(0)

cardRarity = sys.argv[1]
marketPage = sys.argv[2]

marketLink = ""

try:
    if (cardRarity != '0'): 
        marketLink = f'https://theshownation.com/mlb20/community_market?page={marketPage}&display_position=&amp=&max_best_buy_price=&max_best_sell_price=&max_rank=&min_best_buy_price=&min_best_sell_price=&min_rank=&name=&player_type_id=&rarity_id={cardRarity}&series_id=&team_id=&type=mlb_card'
    elif (cardRarity == '0'):
        marketLink = f'https://theshownation.com/mlb20/community_market?page={marketPage}&display_position=&amp;max_best_buy_price=10&amp;max_best_sell_price=&amp;max_rank=&amp;min_best_buy_price=&amp;min_best_sell_price=40&amp;min_rank=&amp;name=&amp;player_type_id=&amp;rarity_id={cardRarity}&amp;series_id=&amp;team_id=&amp;type=mlb_card'

    print(marketLink)
except:
    print("Incorrect Usage")
    print(f"Usage: python3 theshowscraper.py <rarity> <page number>")
    print(f"Rarity: Common = 1, Bronze = 2, etc")


htmlPage = urlopen(marketLink)
soup = BeautifulSoup(htmlPage, features="html.parser")

links = []

for link in soup.find_all('a', href=True):
    if "/mlb20/items" in link['href']:
        if link['href'] not in links:
            links.append(link['href'])


for link in links:
    page = f"https://theshownation.com/{link}?hide_completed_orders=1?hide_trends=1"
    webbrowser.get('chrome').open_new_tab(page)
