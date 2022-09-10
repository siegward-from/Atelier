from exercice2 import nb_occurrences
from exercice2 import position_tri


def agencement(objets: list[int], emplacements: int) -> (list[int], list[int]):
    l = []
    # déplacer de tous les objets dupliqués de la première liste vers la seconde
    for e in objets:
        if nb_occurrences(objets, e) > 1:
            pos = position_tri(objets, e)
            l.append(objets.pop(pos))
    # si la première liste contient encore trop d'objets,
    # déplacez les objets dans la deuxième liste s'ils ne sont pas dupliqués
    if len(objets) > emplacements:
        i = 0
        while len(objets) > emplacements:
            if objets[i] not in l:
                l.append(objets.pop(i))
            else:
                i += 1

    if len(l) > emplacements:
        return False
    return objets, l


print(agencement([1, 2, 2, 3, 4, 5, 5], 4))
# 16 10
