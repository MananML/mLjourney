import requests
import sys

try:
    headers = {
        "Authorization": "Bearer 4d823a4f29f917dffe9832854097e8f6e6be1bdda5c372ef618cdbfddacd2f3c"
    }

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers=headers) 
    
    content = response.json()
    
    btc = content['data']['priceUsd']
    btc = float(btc)
    
    if len(sys.argv) > 1:
        n = sys.argv[1]
        if n.isnumeric:
            n = float(n)
            amount = n * btc
            print(f"${amount:,.4f}")

        else:
            sys.exit("Command-line argument  is not a number.")
    else:
        sys.exit("Missing command-line argument.")

except requests.RequestException:
    print("Error")