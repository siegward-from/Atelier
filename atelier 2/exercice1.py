def somme1(l: list[int]) -> int:
    result = 0
    for i in range(len(l)):
        result += l[i]
    return result


def somme2(l: list[int]) -> int:
    result = 0
    for e in l:
        result += e
    return result


def somme3(l: list[int]) -> int:
    result = 0
    while l:
        result += l.pop(-1)
    return result


def moyenne(l: list[int]) -> float:
    try:
        return somme2(l) / len(l)
    except ZeroDivisionError:
        return 0


def nb_sup1(l: list[int], e: int) -> int:
    result = 0
    for i in range(len(l)):
        if l[i] > e:
            result += 1
    return result


def nb_sup2(l: list[int], e: int) -> int:
    result = 0
    for e1 in l:
        if e1 > e:
            result += 1
    return result


def moy_sup(l: list[int], e: int) -> float:
    return moyenne([element for element in l if element > e])


def val_max(l: list) -> int:
    result = 0
    for e in l:
        if e > result:
            result = e
    return result


def ind_max(l: list) -> int:
    max_value = val_max(l)
    for i in range(len(l)):
        if l[i] == max_value:
            return i


def test_exercice1(func: callable(list), text) -> None:
    print(text)
    print("Test []: ", func([]))
    s = [1, 10, 100, 1000, 10000]
    print("Test [1, 10, 100, 1000, 10000] : ", func(s), '\n')


def test_sup_functions(func: callable((list, int)), text: str) -> None:
    print(text)
    print("Test [], 10: ", func([], 10))
    s = [1, 10, 100, 1000, 10000]
    print("Test [1, 10, 100, 1000, 10000], 10: ", func(s, 10), '\n')


if __name__ == '__main__':
    test_exercice1(somme1, 'Test somme1')
    test_exercice1(somme2, 'Test somme2')
    test_exercice1(somme3, 'Test somme3')
    test_exercice1(moyenne, 'Test moyenne')
    test_sup_functions(nb_sup1, 'Test nb_sup1')
    test_sup_functions(nb_sup2, 'Test nb_sup2')
    test_sup_functions(moy_sup, 'Test moy_sup')
    test_exercice1(val_max, 'Test val_max')
    test_exercice1(ind_max, 'Test ind_max')
