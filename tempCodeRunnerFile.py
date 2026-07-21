import requests
def get_bitcoin_price():
        url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

        try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                bitcoin_price = data["bitcoin"]["usd"]
                print(bitcoin_price)
        except requests.RequesException:
                print("Error! Fetching the bitcoin price.")
                

get_bitcoin_price()

