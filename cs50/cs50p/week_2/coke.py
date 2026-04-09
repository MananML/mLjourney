
AMOUNT = 50
DENOMINATIONS = (5, 10, 25)
print(f"Amount Due: {AMOUNT}")

while True:
    user_input = int(input("Insert Coin: "))

    if user_input in DENOMINATIONS:
        AMOUNT = AMOUNT - user_input
        if  AMOUNT > 0:
            print(f"Amount Due: {AMOUNT}")
        else:
            print(f"Change Owed: {abs(AMOUNT)}")
            break
    else:
        print(f"Amount Due: {AMOUNT}")