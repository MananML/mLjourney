import random


def main():
    right = 0
    wrong = 0


    level = get_level()


    numbers = generate_integer(level)
    xs = []
    ys = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            xs.append(numbers[i])

        else:
            ys.append(numbers[i])

    for _ in range(10):
       

        question = f"{xs[_]} + {ys[_]}"
        answer = eval(question)
        
        for i in range(3):                
            
                user_input = input(f"{question} = ")

                if user_input.isdigit():    
                    if int(user_input) == answer:
                        right += 1
                        break

                    else:
                        print("EEE")
                else:
                    print("EEE")
        else:
            wrong += 1
            print(f"{question} = {answer}")
                        

    print(f"Scored: {right}")

def get_level():
    while True:
        i = input("Level: ")
        if i.isdigit():
            i = int(i)
            if i in range(1, 4):
                return i

def generate_integer(level):
    if level > 1: 
        n = [random.randint(pow(10, level-1), pow(10, level) - 1) for _ in range(20)]

    else:
        n = [random.randint(0, 9) for _ in range(20)]

    return n
    

if __name__ == "__main__":
    main()