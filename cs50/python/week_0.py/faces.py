def convert(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return face

def main():
    inp_ut = input()
    print(convert(inp_ut))
    
main()