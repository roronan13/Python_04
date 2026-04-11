#!usr/bin/env python3

def secure_archive(file_name: str, mode: str = "r",
                   content: str = None) -> tuple[bool, str]:

    if mode == "r":
        try:
            with open(file_name, "r") as file:
                return (True, file.read())
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))

    elif mode == "w":
        try:
            with open(file_name, "w") as file:
                if content is None:
                    content = ""
                file.write(content)
                return (True, content)
        except (FileNotFoundError, PermissionError, Exception) as e:
            return (False, str(e))


if __name__ == "__main__":
    print(" === Cyber Archives Security === ")

    print("\nUsing secure_archive() to read from a nonexistent file : ")
    print(secure_archive("non_existing.txt", "r"))

    print("\nUsing secure_archive() to read from an inaccessible file : ")
    print(secure_archive("no_rights.txt", "r"))

    print("\nUsing secure_archive() to read from a regular file : ")
    result_tuple = secure_archive("test.txt", "r")
    print(result_tuple)

    print("\nUsing secure_archive() to write previous content \
to a new file : ")
    print(secure_archive("new_file.txt", "w", result_tuple[1]))
