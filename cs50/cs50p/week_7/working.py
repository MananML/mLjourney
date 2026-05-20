import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.fullmatch(r"((?:[1-9]|1[0-2]):?(?:[0-5]\d)? (?:AM|PM)) to ((?:[1-9]|1[0-2]):?(?:[0-5]\d)? (?:PM|AM))", s):
        output = []
        patterns = match.groups()

        if patterns[0].split()[1] == "AM":
            if ":" in patterns[0].split()[0]:
                hours, minutes = patterns[0].split()[0].split(":")
                output.append(check_AM(hours, minutes))
            else:
                output.append(check_AM(patterns[0].split()[0], "00"))

        else:
            if ":" in patterns[0].split()[0]:
                hours, minutes = patterns[0].split()[0].split(":")
                output.append(check_PM(hours, minutes))
            else:
                output.append(check_PM(patterns[0].split()[0], "00"))

        if patterns[1].split()[1] == "AM":
            if ":" in patterns[1].split()[0]:
                hours, minutes = patterns[1].split()[0].split(":")
                output.append(check_AM(hours, minutes))
            else:
                output.append(check_AM(patterns[1].split()[0], "00"))

        else:
            if ":" in patterns[1].split()[0]:
                hours, minutes = patterns[1].split()[0].split(":")
                output.append(check_PM(hours, minutes))
            else:
                output.append(check_PM(patterns[1].split()[0], "00"))

        return f"{output[0]} to {output[1]}"

    else:
        raise ValueError

def check_AM(a, b):
    b= str(b).strip(" AM")
    if 1 <= int(a) < 12:
        if b:
            AM_match = f"{int(a):02}:{b}"
        else:
            AM_match = f"{int(a):02}:00"
    else:
        if b:
            AM_match = f"00:{b}"
        else:
             AM_match = "00:00"

    return AM_match

def check_PM(c, d):
    d = str(d).strip(" PM")
    if 1 <= int(c) < 12:
        if d:
            PM_match = f"{int(c) + 12}:{d}"
        else:
            PM_match = f"{int(c) + 12}:00"
    else:
        if d:
            PM_match = f"12:{d}"
        else:
            PM_match = "12:00"

    return PM_match


if __name__ == "__main__":
    main()