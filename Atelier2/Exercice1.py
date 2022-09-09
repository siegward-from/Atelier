def somme1(l: list) -> float:
    result = 0
    for i in range(len(l)):
        result += l[i]
    return result

def somme2(l: list) -> float:
    result = 0
    for e in l:
        result += e
    return result

def somme3(l: list) -> float:
    result = 0
    while l:
        result += l.pop(-1)
    return result

def test_exercice1(func) -> None:
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", func([]))
    #test somme 11111
    S=[1, 10, 100, 1000, 10000]
    print("Test somme 11111 : ", func(S))
if __name__ == '__main__':
    test_exercice1(somme1)
    test_exercice1(somme2)
    test_exercice1(somme3)

def moyenne(l: list) -> float:
    if not len(l):
        return 0
    else:
        return somme2(l) / len(l)

def nb_sup1(l: list, e: int)  -> int:
    result = 0
    for i in range(len(l)):
        if l[i] > e:
            result += 1
    return result

def nb_sup2(l: list, e: int) -> int:
    result = 0
    for e1 in l:
        if e1 > e:
            result += 1
    return result

def moy_sup(l: list, e: int) -> float:
    return moyenne(nb_sup2(l, e))

def val_max(l: list) -> int:
    result = 0
    for e in l:
        if e > result:
            result = e
    return result

def ind_max(l: list) -> int:
    max = val_max(l)
    for i in range(len(l)):
        if l[i] == max:
            return i

#08/09/2022 11:10