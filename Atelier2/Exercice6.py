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
        print("test abscence: ECHEC")

test_present(present)
print()

# question 2
#VERSION 1
def present1(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        else:
            return False
    return False

#VERSION 2
def present2(L, e):
    b = True
    for i in range(len(L)):
        if L[i] == e:
            b = True
        else:
            b = False
    return b
#VERSION 3
def present3(L, e):
    b = True
    for i in range(len(L)):
        return L[i] == e

#VERSION 4
def present4(L, e):
    b = False
    i = 0
    while i < len(L) and b:
        if L[i] == e:
            b = True
    return b

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(present1(l, 1))
print(present2(l, 1))
print(present3(l, 1))
print(present4(l, 1), '\n')

# question 3
#VERSION 1
def present1(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

#VERSION 2
def present2(L, e):
    b = False
    for i in range(len(L)):
        if L[i] == e:
            b = True
            break
    return b
#VERSION 3
def present3(L, e):
    b = True
    for i in range(len(L)):
        if L[i] == e:
            return b
    return False

#VERSION 4
def present4(L, e):
    b = False
    i = 0
    while i < len(L) and not b:
        if L[i] == e:
            b = True
        i += 1
    return b

print(present1(l, 1))
print(present2(l, 1))
print(present3(l, 1))
print(present4(l, 1), '\n')

#question 4
#VERSION 1
def pos1(L, e):
    Lres = list(L)
    for i in range(len(L)):
        if L[i] == e:
            Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e):
    Lres = list(L)
    for i in range(len(L)):
        if L[i] == e:
            Lres[i] = i
    return Lres

# VERSION 3
def pos3(L, e):
    nb = L.count(e)
    Lres = [0] * nb
    for i in range(len(L)):
        if L[i] == e:
            Lres.append(i)
    return Lres

# VERSION 4
def pos4(L, e):
    nb = L.count(e)
    Lres = [0] * nb
    j = 0
    for i in range(len(L)):
        if L[i] == e:
            Lres[j] = i
    return Lres

def test_pos(fonctionPos: callable) -> None:
    if fonctionPos([], 1) == []:
        print("ECHEC: test liste vide")
    else:
        print("SUCCES : test liste vide")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0):
        print("test debut: SUCCES")
    else:
        print("test debut: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9):
        print("test fin: SUCCES")
    else:
        print("test fin: ECHEC")
    if fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
        print("test milieu: SUCCES")
    else:
        print("test milieu: ECHEC")
    if not fonctionPos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10):
        print("test abscence: SUCCES", '\n')
    else:
        print("test abscence: ECHEC", '\n')

l = [3,4,5,7,2,7]
test_pos(pos1)
test_pos(pos2)
test_pos(pos3)
test_pos(pos4)
