import random


def choose_element_list(list_in_which_to_choose: list):
    """ prend en paramètre une liste list_in_which_to_choosede  n'importe  quoi
        et  qui  retourne  un  élément  de  cette  liste  choisi  au hasard """
    return list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)]
