#!usr/bin/env python3

import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 ft_ancient_text.py <file>")
        sys.exit()

    print(" === Cyber Archives Recovery === \n")

    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}' : {e}")
        sys.exit()
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}' : {e}")
        sys.exit()

    print(" --- ")
    text: str = file.read()
    print(text)
    print(" --- ")

    file.close()
    print(f"File '{sys.argv[1]}' closed.")

    file = open(sys.argv[1], "rw")
    old_text: str = file.read()

    new_text: str = ""
    old_lines: list[str] = old_text.split('\n')
    for old_line in old_lines:
        new_line = old_line + "#\n"
        new_text += new_line
        
