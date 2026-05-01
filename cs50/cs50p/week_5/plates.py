
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
    
    instance = 0
    while True:
        if check_str(s):
            for _, i in enumerate(s):
                if i.isalpha():
                    for chr in s[:_]:
                        if chr.isdigit():
                            return False
            
            else:
                for _, i in enumerate(s):
                    if i.isdigit():
                        for chr in s[_:]:
                            if chr[0] == "0":
                                return False
                            else:
                                return True
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


if __name__ == "__main__":
    main()