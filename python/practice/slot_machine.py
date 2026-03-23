import random

ROWS = 3
COLUMNS = 3

MIN_DEPOSIT = 30
MAX_DEPOSIT = 300

MAX_LINE = 3
MIN_LINE = 1

MAX_BET = 50
MIN_BET = 10

SYMBOLS = {
    "🍀": 4, 
    "🌰": 5,
    "🥝": 7,
    "🍇": 5,
    "🌚": 6
}

SYMBOLS_VALUE = {
    "🍀": 7, 
    "🌰": 5,
    "🥝": 4,
    "🍇": 6,
    "🌚": 4
}
 
def get_slot_machin_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, value in symbols.items():
        for _ in range(value):
            all_symbols.append(symbol)
        
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine_spin(slots, rows):
    for row in range(rows):
        for column in slots:
            print(column[row], end="")

        print()

def check_winning(slots, lines, value, bet):
    winning = 0
    lines_won_on = []

    for line in range(lines):
        symbol = slots[0][line]

        for _ in slots:
            symbol_to_check = _[line]

            if symbol_to_check != symbol:
                break

        else:
            winning = value[symbol] * bet
            lines_won_on.append(line + 1)

    return winning, lines_won_on

def deposit():
    while True:
        deposit = input("How much would you like to deposit? ")
        if deposit.isdigit():
            deposit = int(deposit)
            if MIN_DEPOSIT <= deposit <= MAX_DEPOSIT:
                return(deposit)
            print("please input a digit in the range (30 - 300).")

        else:
            print("Please input a digit.")

def lines():
    while True:
        lines = input("How many lines do you want to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINE <= lines <= MAX_LINE:
                return(lines)
            else:
                print("Please input a digit in the range (1 - 3).")

        else:
            print("please input a digit.")

def bet():
    while True:
        bet = input("How much do you want to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return(bet)
            else:
                print("Please enter a digit in the range (10 - 50).")

        else:
            print("Please enter a digit.")






def main():
    print("___SLOT MACHINE___")

    balance = deposit()
    n_lines = lines()
    n_bet = bet()

    slots = get_slot_machin_spin(ROWS, COLUMNS, SYMBOLS)
    print(f"Your current balance is {balance}")
    print_slot_machine_spin(slots, ROWS)

    winning, lines_won_on = check_winning(slots, n_lines, SYMBOLS_VALUE, n_bet)
    
     


main()



















"""

    ___SLOT MACHINE___


    How much would you like to deposit (50-300)
    how many lines do you want to bet on.
    how much do tyou want to bet on each line 
    
    you current balance is ...............
    outtttttttttttt

    you won 0                  or you won.............

    your current balance is ...... 
    bet again (y/ n)



    
"""





















