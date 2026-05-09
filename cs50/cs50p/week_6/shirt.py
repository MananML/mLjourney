import sys
from PIL import Image, ImageOps

def check_user_input():
    if len(sys.argv) == 3:
        for file in sys.argv[1:3]:
            if not file.lower().endswith((".jpg", ".jpeg", ".png")):
                sys.exit("Invalid input.")                        
        else:
            if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
                sys.exit("Input and out put have different extensions.")
            return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")

    else:
        sys.exit("Too many command-line arguments.")

def overlay():
    fisrt_image, second_image = check_user_input()
    cs50_shirt = "shirt.png"

    with Image.open(cs50_shirt) as foreground, Image.open(fisrt_image) as background:
        size = foreground.size

        resized_background = ImageOps.fit(background, size)

        resized_background.paste(foreground, (0, 0), foreground)
    
    return resized_background, second_image

def main():
    cs50_shirt, image_file = overlay()

    cs50_shirt.save(image_file)

if __name__ == "__main__":
    main()