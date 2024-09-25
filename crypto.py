import requests
import json

def getCoinValue(coinName):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coinName}&vs_currencies=eur"
    response = requests.get(url)
    data = json.loads(response.text)
    result = f"{coinName}: €{data[coinName]['eur']}"
    return result

def trending():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

print(trending())