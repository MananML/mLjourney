import random

MAX_PLAYERS = 3
MIN_PLAYERS = 1

DICE_VALUES = (1, 2, 3, 4, 5, 6)

def user_input():
    players = input("How many opponents? ")
    if players.isdigit:
        players = int(players)
        if players < MIN_PLAYERS:
            print("Input less than the minimum amount of player.")
        elif players > MAX_PLAYERS:
            print("Input greater than the maximum amount of players.")
        else:
            return players
    else:
        print("Enter the number of opponents you wish to play against.")

def rolled_dice():
    x = random.choices(DICE_VALUES, k=2)


    print("\n")
    










"""
white boxes = 48
player boxes = 6

total boxes = 48 + 6 * 4
total boxes = 72

functionality:
if another users end point is on top another, return.
require two dice
require six two come out.
ask the user how many players they want to face.
"""