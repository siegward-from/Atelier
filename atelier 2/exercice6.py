# question 1
def present(l: list, e: int) -> bool:
    return e in l


def test_present(present: callable) -> None:
    if present([], 1):
        print("ECHEC: test liste vide")
    else:
        print("SUCCES : test liste vide")
    if present([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0):
        print("test debut: SUCCES")
    else:
        print("test debut: ECHEC")
    if present([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9):
        print("test fin: SUCCES")
    else:
        print("test fin: ECHEC")
    if present([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
        print("test milieu: SUCCES")
    else:
        print("test milieu: ECHEC")
    if not present([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10):
        print("test abscence: SUCCES")
    else:
        print("test abscence: ECHEC \n")


test_present(present)


# question 2
# VERSION 1
def present1(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return True
        else:
            return False
    return False


# VERSION 2
def present2(l, e):
    b = True
    for i in range(len(l)):
        if l[i] == e:
            b = True
        else:
            b = False
    return b


# VERSION 3
def present3(l, e):
    b = True
    for i in range(len(l)):
        return l[i] == e


# VERSION 4
def present4(l, e):
    b = False
    i = 0
    while i < len(l) and b:
        if l[i] == e:
            b = True
    return b


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(present1(l, 1))
print(present2(l, 1))
print(present3(l, 1))
print(present4(l, 1), '\n')


# question 3
# VERSION 1
def present1(l: list[int], e: int) -> bool:
    for i in range(len(l)):
        if l[i] == e:
            return True
    return False


# VERSION 2
def present2(l: list[int], e: int) -> bool:
    b = False
    for i in range(len(l)):
        if l[i] == e:
            b = True
            break
    return b


# VERSION 3
def present3(l: list[int], e: int) -> bool:
    b = True
    for i in range(len(l)):
        if l[i] == e:
            return b
    return False


# VERSION 4
def present4(l: list[int], e: int) -> bool:
    b = False
    i = 0
    while i < len(l) and not b:
        if l[i] == e:
            b = True
        i += 1
    return b


print('test present1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1):', present1(l, 1))
print('test present2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1):', present2(l, 1))
print('test present3([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1):', present3(l, 1))
print('test present4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1):', present4(l, 1), '\n')


# question 4
# VERSION 1
def pos1(l: list[int], e: int) -> list[int]:
    lres = []
    for i in range(len(l)):
        if l[i] == e:
            lres.append(i)
    return lres


# VERSION 2
def pos2(l: list[int], e: int) -> list[int]:
    lres = []
    for i in range(len(l)):
        if l[i] == e:
            lres.append(i)
    return lres


# VERSION 3
def pos3(l: list[int], e: int) -> list[int]:
    lres = []
    for i in range(len(l)):
        if l[i] == e:
            lres.append(i)
    return lres


# VERSION 4
def pos4(l: list[int], e: int) -> list[int]:
    lres = []
    for i in range(len(l)):
        if l[i] == e:
            lres.append(i)
    return lres


def test_pos(fonctionPos: callable, text: str) -> None:
    print(text)
    if fonctionPos([], 1) == []:
        print("test liste vide: SUCCES")
    else:
        print("test liste vide: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == [0]:
        print("test debut: SUCCES")
    else:
        print("test debut: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == [9]:
        print("test fin: SUCCES")
    else:
        print("test fin: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [4]:
        print("test milieu: SUCCES")
    else:
        print("test milieu: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == []:
        print("test abscence: SUCCES", '\n')
    else:
        print("test abscence: ECHEC", '\n')


test_pos(pos1, 'test pos1')
test_pos(pos2, 'test pos2')
test_pos(pos3, 'test pos3')
test_pos(pos4, 'test pos4')
