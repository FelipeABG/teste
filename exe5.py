def reverse_string(string: str) -> str:
    k: int = len(string) - 1
    new_string: str = ""

    while k >= 0:
        new_string += string[k]
        k -= 1

    return new_string


string: str = input("Your string: ")
print(reverse_string(string))
