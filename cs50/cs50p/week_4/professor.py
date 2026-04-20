import random

levels = [1, 2, 3]

def main():
    ...


def get_level():
    while True:
        level = input("Level: ")

        if level.isdigit() and level in levels:
            level = int(level)
            return level

def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
