import random

levels = ["1", "2", "3"]

def main():
    level = get_level()
    for i in range(11):
        x, y = generate_integer(level)

        question = input(f"{x} + {y} = ")
        answer = eval(question)

        if question == answer:
            continue
            
        for _ in range(3):
            if question == answer:
                break
        else:
            print(answer)  
            


def get_level():
    while True:
        level = input("Level: ")

        if level.isdigit() and level in levels:
            level = int(level)
            return level

def generate_integer(level):
    x = random.randint(0, pow(10, level))
    y = random.randint(0, pow(10, level))    

    pair = x, y
    return pair

if __name__ == "__main__":
    main()
