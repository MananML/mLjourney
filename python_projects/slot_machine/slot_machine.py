
# imported a module called random
import random

ROWS = 3
COLUMNS = 3

MIN_DEPOSIT = 50
MAX_DEPOSIT = 1000

MAX_LINE = 3
MIN_LINE = 1

MAX_BET = 50
MIN_BET = 10

# symbols to be printed on our slot machine 
SYMBOLS = {
    "🍀": 8, 
    "🌰": 11,
    "🥝": 17,
    "🍇": 10,
    "🌚": 16
}

# the value of each symbol when calculating your win 
SYMBOLS_VALUE = {
    "🍀": 7, 
    "🌰": 5,
    "🥝": 4,
    "🍇": 6,
    "🌚": 4
}

# the amount the player wants to deposit
def deposit():
    while True:
        deposit = input("How much would you like to deposit? ")
        if deposit.isdigit():
            deposit = int(deposit)
            if MIN_DEPOSIT <= deposit <= MAX_DEPOSIT:
                return(deposit)
            print(f"please input a digit in the range ({MIN_DEPOSIT} - {MAX_DEPOSIT}).")

        else:
            print("Please input a digit.")

# The number of lines the user want to bet on 
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

# the amount the want to bet on each line
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

# the machine spin
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

# print the symbols after they have been spun
def print_slot_machine_spin(slots, rows):
    for row in range(rows):
        for i, column in enumerate(slots):            
            if i < len(slots) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")

        print()

# check how much the player won and in what line
def check_winning(slots, lines, value, bet):
    winning = []
    lines_won_on = []

    for line in range(lines):
        symbol = slots[0][line]

        for _ in slots:
            symbol_to_check = _[line]

            if symbol_to_check != symbol:
                break

        else:
            winning.append(value[symbol] * bet)
            lines_won_on.append(line + 1)

    return winning, lines_won_on

def spin(balance, total_bet, n_bet, n_lines):

    while True:
        if total_bet > balance:
            print(f"\nYou do not have enough amount, your current balance is ${balance}.\n")
            print(f"You left with ${balance}")
            print("____THANKS FOR PLAYING____")
            quit()
        else:
            break

    print(f"You are betting ${n_bet} on {n_lines} line, your total bet is ${total_bet}.\n") 
    slots = get_slot_machin_spin(ROWS, COLUMNS, SYMBOLS)
    print_slot_machine_spin(slots, ROWS)

    winning, lines_won_on = check_winning(slots, n_lines, SYMBOLS_VALUE, n_bet)
    winning = sum(winning)
    print(f"\nYou won ${winning}.")

    if winning > 0:
        print("You won on line:", *lines_won_on)
     
    return winning - total_bet

def main():

    print("___SLOT MACHINE___")
    balance = deposit()
    n_lines = lines()
    n_bet = bet()
    total_bet = n_bet * n_lines

    while True:
        print(f"Current balance is ${balance}")
        _ = input("PRESS ANY BUTTON TO SPIN (Q TO QUIT) ")
        if _ == "q".lower():
            break
        balance += spin(balance, total_bet, n_bet, n_lines)

    print(f"You left with ${balance}")
    print("____THANKS FOR PLAYING____")


main()