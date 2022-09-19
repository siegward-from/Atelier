from exercice2 import nb_occurrences


def agencement(objets: list[int], emplacements: int) -> (list[int], list[int]):
    list_ = []

    # déplacer de tous les objets dupliqués de la première liste vers la seconde
    for e in objets:
        if nb_occurrences(objets, e) > 1:
            objets.remove(e)
            list_.append(e)

    # si la première liste contient encore trop d'objets,
    # creer une nouvelle liste avec les objets qu'il faut deplacer
    if len(objets) > emplacements:
        el_to_move = [el for el in objets if el not in list_]
        el_to_move = el_to_move[:len(objets) - emplacements]
        for el in el_to_move:
            objets.remove(el)
            list_.append(el)

    if len(list_) > emplacements:
        return False
    return objets, list_


print(agencement([1, 3, 4, 5, 2, 2, 0, 0], 4))
