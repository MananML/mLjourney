
MAX_CH = 6
MIN_CH = 2
PUNTUATION = (".", " ", ",", ";")

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):    
    while True:
        if check_str(s):
            for i in s[:-1]:
                if i.isdigit() and i == 0:
                    return False
                elif i.isdigit() and s[-1].isalpha():
                    return False
                else:
                    return True
        else:
            return False

def check_str(s):
    if MIN_CH <= len(s) <= MAX_CH:
        if s[0].isalpha() and s[1].isalpha():
            for i in s:
                if i in PUNTUATION:
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False

main()