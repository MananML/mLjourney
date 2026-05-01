
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def main():
    user_input = input("Input: ")

    output = shorten(user_input)

    print(output)

def shorten(word):
    for i in word:
        if i in VOWELS:
            word = word.replace(i, "")
    
    return word


if __name__ == "__main__":
    main()