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

    file = open(sys.argv[1], "r")
    old_text: str = file.read()

    print("\nTransform data : ")
    print(" --- ")
    new_text: str = ""
    old_lines: list[str] = old_text.split('\n')
    for old_line in old_lines:
        new_line = old_line + "#\n"
        new_text += new_line

    print(new_text, end="")
    print(" --- ")

    new_file_name: str = input("\nEnter new file name to save transformed \
data (empty won't save anything)\n")
    if new_file_name == "":
        print("Not saving data\n")
        sys.exit()
    else:
        print(f"\nSaving data to '{new_file_name}'")
        try:
            new_file = open(new_file_name, "w")
            new_file.write(new_text)
            print(f"Data saved in '{new_file_name}'\n")
        except Exception as e:
            print(f"Error creating or writing new file : {e}\n")

    new_file = open(new_file_name, "r")
    text_in_new_file: str = new_file.read()
    print(text_in_new_file)
    new_file.close()
    print(f"File '{new_file_name}' closed.")
