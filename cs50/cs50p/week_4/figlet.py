import sys
import random
from pyfiglet import Figlet

def main():

    font_parameter = ["-f", "--font"]
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        if not (sys.argv[1] in font_parameter and sys.argv[2] in fonts):
            sys.exit("Input a valid font/font parameter")
        else:
            figlet.setFont(font=sys.argv[2])

    elif len(sys.argv) == 1:
        new_font = random.choice(fonts) 
        figlet.setFont(font=new_font)   

    else:
        sys.exit("Input a valid font/font parameter")


    text = input("Input: ")
    ctext = figlet.renderText(text)


    print(f"Output: {ctext}")

if __name__ == "__main__":
    main()
