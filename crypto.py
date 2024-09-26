import requests
import json

def getCoinValue(coinName):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coinName}&vs_currencies=eur"
    response = requests.get(url)
    data = json.loads(response.text)
    result = f"{coinName}: €{data[coinName]['eur']}"
    return result

def trending():
    finalList = ""
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = json.loads(response.text)
    
    for coin in data['coins'][:5]:
        extractedName = coin['item']['name']
        extractedPrice = coin['item']['data']['price']
        finalList += f"{extractedName} at ${extractedPrice} \n"

    return finalList