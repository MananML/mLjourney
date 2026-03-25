SPEED = 3 * pow(10, 8)

def calculate(mass):
    energy = mass * pow(SPEED, 2)

    return energy

def main():
    mass = int(input("m: "))
    print(f"E: {calculate(mass)}")

main()