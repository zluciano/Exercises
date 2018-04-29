def invert_lines(text):
    file = open(text, "r")
    lines = file.readlines()
    file.close()
    file = open("texto_invertido.txt", "w")
    for i in range(0, len(lines)):
        file.write(lines[len(lines)-i-1])
    file.close()