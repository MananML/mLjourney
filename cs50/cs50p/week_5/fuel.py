def main():
    fraction = input("Fraction: ")
    perc = convert(fraction)
    tank_level = gauge(perc)
    print(tank_level)


def convert(fraction):
    if "/" in fraction:
        x, y = fraction.split("/")

        if x.isdigit() and y.isdigit():
            x, y = int(x), int(y)
        
            if x <= y and x > -1:
                perc = int(round(x/y * 100))
                return perc
        
            elif y == 0:
                raise ZeroDivisionError
            
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError
    
def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()