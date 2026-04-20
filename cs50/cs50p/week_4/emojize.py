import emoji

def user_input():
    emo = input("Input: ")
    return emoji.emojize(emo, language = "alias")

def main():
    print(user_input())

if __name__ == "__main__":
    main()