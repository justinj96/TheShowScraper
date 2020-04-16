from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import webbrowser
import sys

marketPage = sys.argv[1]

marketLink = ""

try:
    marketLink = "https://theshownation.com/mlb20/community_market?page=" + marketPage + "&display_position=&amp=&max_best_buy_price=&max_best_sell_price=&max_rank=&min_best_buy_price=&min_best_sell_price=&min_rank=&name=&player_type_id=&rarity_id=1&series_id=&team_id=&type=mlb_card"
except:
    print("Invalid Page Number")


htmlPage = urlopen(marketLink)
soup = BeautifulSoup(htmlPage, features="html.parser")

links = []

for link in soup.find_all('a', href=True):
    if "/mlb20/items" in link['href']:
        if link['href'] not in links:
            links.append(link['href'])

print(len(links))

# for link in links:
#     webbrowser.get('chrome').open_new_tab("https://theshownation.com/" + link)