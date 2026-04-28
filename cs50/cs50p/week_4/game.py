import random

def level():
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level > 0:
                return level
        else:
            print("Please enter a digit.")

def users_guess():
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess > 0:
                return guess

def check_guess(number):
    while True:
        guess = users_guess()
        if guess == number:
            print("Just right!")
            break
        else:
            if guess > number:
                print("Too large!")
            else:
                print("Too small!")

def main():
    n = level()
    number = random.randint(1, n)

    check_guess(number)

main()
