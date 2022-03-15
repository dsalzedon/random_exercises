from typing import List


def first_duplicate(my_lst: List) -> int:

    duplicates = check_duplicate(my_lst)

    return check_minor_duplicate(duplicates) if len(duplicates) > 0 else -1


def check_duplicate(lst: List) -> dict:

    my_dups = {}

    for x in range(len(lst)):
        nw_lst = lst[:]
        nw_lst.pop(x)
        if lst[x] in nw_lst and lst[x] not in my_dups:
            my_dups[lst[x]] = nw_lst.index(lst[x])

    return my_dups


def check_minor_duplicate(my_dups: dict) -> int:

    sorted_dups = (sorted(my_dups.items(), key=lambda item: item[1]))

    return sorted_dups[0][0]


def main():
    a = [[2, 1, 3, 5, 3, 2], [2, 2], [2, 4, 3, 5, 1]]
    # test 1, expecting 3
    # test 2, expeting 2
    # text 3, expeccting -1
    for x in a:
        print(first_duplicate(x))

if __name__ == "__main__":
    main()
