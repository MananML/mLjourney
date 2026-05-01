
def main():
    user_input = input("Greeting: ").lower().strip()
    output = value(user_input)

    print(output)

def value(greeting):
    first_word = greeting.split()[0]
    first_letter = greeting[0]

    if first_word == "hello" or first_word == "hello,":
        return 0

    elif first_letter == "h":
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()


