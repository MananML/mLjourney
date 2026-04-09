
camelCase = input("camelCase: ")

for i in camelCase:
    if i.isupper():
        camelCase = camelCase.replace(i, f"_{i.lower()}")

print(f"snake_case: {camelCase}")

