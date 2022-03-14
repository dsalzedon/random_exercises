from typing import List


def first_duplicate(my_lst: List) -> int:
    duplicates = check_duplicate(my_lst)

    return check_minor_duplicate(duplicates) if len(duplicates) > 0 else -1


def check_duplicate(lst: List) -> dict:
    """
    Crea un diccionario de duplicados
    Crea una copia de la lista para comparar los elementos
    Checa si el elemento se encuentra en la copia
    si está, agrega el elemento y su indice, al dict
    """
    my_dups = {}

    for x in range(len(lst)):
        nw_lst = lst[:]
        nw_lst.pop(x)  # elimina el elemento de ese indice de la nueva lista
        for y in range(len(nw_lst)):
            # la comparacion va primero en el AND para evitar q haga la segunda condicion en caso de q no sean iguales
            # uso un AND para evitar poner dos if, y así evitar q aumente la complejidad (mcabee)
            if lst[x] == nw_lst[y] and lst[x] not in my_dups:
                # agrega el elemento y el indice al dict
                my_dups[lst[x]] = y + 1

    return my_dups


def check_minor_duplicate(my_dups: dict) -> int:
    """
    Ordena el dict de menor a mayor de acuerdo a los Values
    Convierte el dict a una lista de tuplas
    con el primer elemento siendo Keys y el segundo Value (Keys, Values) del dict
    Retorna el primer elemento de la primera tupla (el Key con el menor Value)
    """
    sorted_dups = (sorted(my_dups.items(), key=lambda item: item[1]))
    print(sorted_dups)
    return sorted_dups[0][0]


a = [[2, 1, 3, 5, 3, 2], [2, 2], [2, 4, 3, 5, 1]]
# test 1, expecting 3
# test 2, expeting 2
# text 3, expeccting -1
for x in a:
    print(first_duplicate(x))
