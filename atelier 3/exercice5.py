from exercice4 import presente


def ouvrante(car: str) -> bool:
    """ :return Un booléen indiquant si le caractère est une parenthèse, un crochet ou une accolade ouvrante """
    return car in ['(', '[', '{']


def fermante(car: str) -> bool:
    """ :return Un booléen indiquant si le caractère est une parenthèse, un crochet ou une accolade fermante """
    return car in [')', ']', '}']


def renverse(car: str) -> str:
    """
    :return Un caractère. Selon que le paramètre soit une parenthèse, un crochet ou une accolade fermante,
    la fonction renvoie une parenthèse, un crochet ou une accolade ouvrante.
    Si le paramètre est un nombre, un espace, un opérateur ou une parenthèse,accolade ou crochet fermant,
    la fonction renvoie le caractère lui-même.
    """
    if fermante(car):
        return ('(', '[', '{')[presente([')', ']', '}'], car)]
    else:
        return car


def operateur(car: str) -> bool:
    """ :return  Un booléen indiquant si le caractère est un opérateur (+, - ou *) """
    return car in ('+', '-', '*')


def nombre(car: str) -> bool:
    """ Un booléen indiquant si la chaine est un nombre """
    return car.isdigit()


def caractere_valid(car: str) -> bool:
    """
    :return Un booléen indiquant si la chaine est un nombre
    c'est-à-dire qu’elle ne comporte que des caractères numériques
    """
    return any([ouvrante(renverse(car)), operateur(car), nombre(car), car == ' '])


def verif_parenthese(expression: str) -> bool:
    """
    :return Un booléen indiquant si l’expression arithmétique contenue dans le texte est valide
    (ne comportant que des caractères valides) et correctement parenthésée ou non
    """
    pile = []
    for car in expression:
        if not caractere_valid(car):
            return False
        if ouvrante(car):
            pile.append(car)
        elif fermante(car):
            try:
                if pile.pop(-1) != renverse(car):
                    return False
            except IndexError:
                return False
    return not pile


def test_verif_paranthese():
    assert verif_parenthese('(3+2) * 6-1') is True
    assert verif_parenthese('([3+2)] * 6-1') is False
    assert verif_parenthese('((3+2)*6-1') is False
    assert verif_parenthese('(5+7]*12') is False


if __name__ == '__main__':
    test_verif_paranthese()
