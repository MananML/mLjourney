MIN_DEPOSIT = 30
MAX_DEPOSIT = 300

MAX_LINE = 3
MIN_LINE = 1

MAX_BET = 50
MIN_BET = 10

symbols = {
    "🍀":
    "🌰":
    "🥝":
    "🍇":
    "🌚":
}




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
            if MAX_LINE <= lines <= MIN_LINE:
                return(lines)
            else:
                print("Please input a digit in the range (1 - 3).")

        else:
            print("please input a digit.")

def bet():
    bet = input("How much do you want to bet on esch line? ")
    if bet.isdigit():
        bet = int(bet)
        if MIN_BET <= bet <= MAX_BET:
            return(bet)
        else:
            print("Please enter a digit in the range (10 - 50).")

    else:
        print("Please enter a digit.")






















"""
    How much would you like to deposit (50-300)
    how many lines do you want to bet on.
    how much do tyou want to bet on each line 
    
    
    outtttttttttttt


    your current balnace is 

    bet again (y/ n)



    
"""






















