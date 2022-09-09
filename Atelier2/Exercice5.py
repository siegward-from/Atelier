from Exercice2 import nb_occurrences
from Exercice2 import position_tre

def agencement(emplacements, objets):
    l = []
    for e in objets:
        if nb_occurrences(objets, e) > 1:
            pos = position_tre(objets, e)
            l.append(objets.pop(pos))
    if len(objets) > emplacements:
        i = 0
        while len(objets) > emplacements:
            if objets[i] not in l:
                l.append(objets.pop(i))
            else:
                i += 1
    return (objets, l)

print(agencement(4, [1, 2, 2, 3, 4, 5, 5]))
#16 10