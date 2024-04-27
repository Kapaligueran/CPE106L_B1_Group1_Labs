file = input('Input a file name: ')
lines = []  # Changed variable name to 'lines' to avoid confusion
with open(file, 'r') as f:
    for line in f:  # Changed variable name to 'line' to iterate over lines
        lines.append(line.strip())
    print("The file", file, "has", len(lines), "lines.")
    while True:
        if len(lines) == 0:
            break
        lineNumber = int(input("Input a line number [or 0 to quit]: "))
        if lineNumber == 0:
            break
        elif lineNumber > len(lines):
            print("ERROR: Line number must be less than or equal to", len(lines))
        else:
            print(lineNumber, ": ", lines[lineNumber - 1], "\n")
