import random


def gen_list_random_int(int_bnr: int = 10, int_binf: int = 0, int_bsup: int = 10) -> list:
    """ :return une liste de nombres aléatoires int_nbrcompris entre int_binfet int_bsup """
    return [random.randint(int_binf, int_bsup) for _ in range(int_bnr)]
