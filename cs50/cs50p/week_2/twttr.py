
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
user_input = input("Input: ")

for i in user_input:
    if i in VOWELS:
        user_input = user_input.replace(i, "")

print(user_input)