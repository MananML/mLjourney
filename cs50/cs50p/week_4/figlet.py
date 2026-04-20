import sys
import random
from pyfiglet import Figlet

font_parameter = ["-f", "--font"]

def convert(s):
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        if sys.argv[1] in font_parameter and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        
        else:
            sys.exit("Input a valid font/font parameter")
        
    elif len(sys.argv) == 1:
        new_font = random.choice(fonts) 
        figlet.setFont(font=new_font)   

    else:
        sys.exit("wrong input")

    return figlet.renderText(s)

def main():
    text = input("Input: ")

    print(convert(text))

main()
