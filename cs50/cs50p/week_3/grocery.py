
def main():
    items = {} 

    while True:
        try:
            item = input()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

        except EOFError:
            break
        
    sorted_items = dict(sorted(items.items()))
    for key, value in sorted_items.items():
        print(value, key.upper()) 
    

main()