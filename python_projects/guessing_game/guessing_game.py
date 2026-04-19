import random
import time

GUESS = 0

def get_users_input():
    while True:
        number = input("Input a number to guess in that range: ")
        if number.isdigit():
            number = int(number)
            if number <= 10:
                print("Please input a number greater than ten.")
        else:
            print("Please input a digit.")
        
        return number

def check_users_guess(number):
    global GUESS
    while True:
        guess = input("Make a guess: ")
        GUESS += 1
        if guess.isdigit():
            guess = int(guess)
            if guess == number:
                print("You guessed right.")
                break
            else:
                print("You guessed wrong.")
                if guess < number:
                    print("Your guess is less than the required number")
                elif guess > number:
                    print("Your guess is greater than the required number.")
            _ = input("Press enter to guess again(q to quit) ")
            if _ == "q":
                break             
        else:   
            print("Please input a digit.")

def main():
    guessing_range = get_users_input()
   
    random_number = random.randint(0, int(guessing_range))
    start = time.time()
    check_users_guess(random_number)

    print(f"The number was {random_number}")
    print(f"You guessed {GUESS} times.")
    end = time.time()
    total_time = end - start
    print(f"You spent {round(total_time)} seconds guessing.")
    

main()