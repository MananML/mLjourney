import inflect
p = inflect.engine()

def adieu(names):
    return p.join(names)

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        
        except EOFError:
            break

    print(f"\nAdieu, adieu, to {adieu(names)}")

main()