def first_not_repeating_char(my_string: str) -> str:
    no_duplicates = check_duplicates(my_string)

    return "_" if check_minor_duplicate(no_duplicates) == None else check_minor_duplicate(no_duplicates)


def check_duplicates(my_str: str) -> dict:
    no_duplicates = {}
    for x in my_str:
        try:
            no_duplicates[x] += 1
        except Exception:
             no_duplicates[x] = 1

    return no_duplicates


def check_minor_duplicate(my_dups: dict) -> str:

    for x in my_dups:
        if my_dups[x] == 1:
            return x


def main():
    s = ["abacabad", "abacabaabacaba"]
    # test1, expected c
    # test2, expected '_'
    for x in s:
        print(first_not_repeating_char(x))


if __name__ == "__main__":
    main()
