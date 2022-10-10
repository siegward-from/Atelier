import random


def mix_list(list_to_mix: list) -> list:
    """ prend en paramètre une liste list_to_mixde n'importe quoi potentiellement triée
        et qui retourne la liste mélangée. """
    copy_list = list_to_mix[:]
    len_copy_list = len(copy_list)
    for i in range(len_copy_list):
        copy_list.append(copy_list.pop(random.randint(0, len_copy_list - 1)))
    return copy_list
