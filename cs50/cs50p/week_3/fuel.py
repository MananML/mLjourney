
def check_fraction(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)

            if x <= y and x > -1:
                value = int(round(x/y * 100))
                if value >= 99:
                    return "F"
                elif value <= 1:
                    return "E"
                else:
                    return f"{value}%"
            else:
                break

        except (ValueError, ZeroDivisionError):
            break

def main():
    while True:
        fraction = input("Fraction: ")
        tank_level = check_fraction(fraction)
        if tank_level != None:
            print(tank_level)
            break


main()