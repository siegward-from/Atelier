from exercice3 import *


def extract_elements_list(list_in_which_choose: list, int_nbr_of_element_to_extract: int = 2) -> list:
    """ prend     en     paramètre     une     liste list_in_which_to_choosede n'importe quoi,
        un int_nbr_of_element_to_extractet qui retourne
        une  liste  composée  de int_nbr_of_element_to_extractéléments de  la  liste  de  départ  choisis  au hasard """
    return [choose_element_list(list_in_which_choose) for _ in range(int_nbr_of_element_to_extract)]
