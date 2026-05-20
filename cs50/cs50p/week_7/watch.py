import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"<iframe src=\"(https?)://(?:www\.)?youtube\.com/embed/(\w+)\"></iframe>", s):
        
        mod_match = f"https://youtu.be/{match.group(2)}"
        return mod_match

if __name__ == "__main__":
    main()