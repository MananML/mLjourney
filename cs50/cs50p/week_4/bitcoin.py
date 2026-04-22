import requests
import json

try:
    headers = {
        "Authorization": "Bearer 4d823a4f29f917dffe9832854097e8f6e6be1bdda5c372ef618cdbfddacd2f3c"
    }

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers=headers) 
    
    content = response.json()
    
    btc = content['data']['priceUsd']
    print(btc)

except requests.RequestException:
    print("Error")