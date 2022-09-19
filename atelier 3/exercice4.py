from exercice2 import mots_n_lettres


def mot_correspond(mot: str, motif: str) -> bool:
    """
    :return True ou False suivant que la chaine de caractère mot correspond, ou pas,
            à la chaine de caractères motif donnée
    """
    try:
        return all([motif[i] == mot[i] for i in range(len(motif)) if motif[i] != '.'])
    except IndexError:
        return False


def presente(mot: str | list[str], lettre: str) -> int:
    """ :return un entier représentant l’indice de la lettre passée en paramètre dans la chaine de caractères mot """
    for i, lettre_ in enumerate(mot):
        if lettre_ == lettre:
            return i
    return -1


def mot_possible(mot: str, lettres: str) -> bool:
    """ :return True ou False suivant que le mot peut s'obtenir avec les lettres passées en paramètres """
    return all([lettre in lettres for lettre in mot])


def mot_optimaux(dico: list[str], lettres: str) -> list[str]:
    max_longeur = max([len(mot) for mot in dico])
    return [mot for mot in mots_n_lettres(dico, max_longeur) if mot_possible(mot, lettres)]
