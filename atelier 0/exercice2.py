TARIF_VERTE = {
    20: 1.16,
    100: 2.32,
    250: 4,
    500: 6,
    1000: 7.5,
    3000: 10.5
}
TARIF_PRIORITAIRE = {
    20: 1.43,
    100: 2.86,
    250: 5.26,
    500: 7.89,
    3000: 11.44
}
TARIF_ECOPLI = {
    20: 1.14,
    100: 2.28,
    250: 3.92
}
TARIF_OUTRE_MER = {
    0.5: 8.35,
    1: 11.20,
    2: 14.10,
    5: 23.65,
    10: 37.50,
    15: 75.85,
    30: 87.40
}


def calcul_tarif(tarif: dict, weight_letter) -> float:
    for key in list(tarif.keys()):
        if weight_letter <= key:
            return tarif[key]


def calcul_cost_letter(type_letter: str, weight_letter: int, to_zone: int, have_sticker: bool) -> float:
    """
    :param type_letter: (str)[verte, prioritaire, ecopli, outre-mer]
    :param weight_letter: (int)
    :param to_zone: (int)[1, 2]
    :param have_sticker: (bool)
    :return: prix net (float)
    """
    summe = 0
    final_weight = weight_letter // 10
    if weight_letter % 10 != 0:
        final_weight += 1
    if have_sticker:
        summe += 0.5

    match type_letter:
        case 'verte':
            summe += calcul_tarif(TARIF_VERTE, weight_letter)
            summe += final_weight * [0.05, 0.11][to_zone - 1]
        case 'prioritaire':
            summe += calcul_tarif(TARIF_PRIORITAIRE, weight_letter)
            summe += final_weight * [0.05, 0.11][to_zone - 1]
        case 'ecopli':
            summe += calcul_tarif(TARIF_ECOPLI, weight_letter)
            summe += final_weight * [0.02, 0.5][to_zone - 1]
        case 'outre-mer':
            summe += calcul_tarif(TARIF_OUTRE_MER, weight_letter)
    return round(summe, 2)


if __name__ == '__main__':
    print('Affranchissement postal')
    type_letter = input('Type de colis(verte, prioritaire, ecopli, outre-mer): ')
    weight_letter = int(input('Poids du colis: '))
    to_zone = int(input('Vers zone(1, 2): '))
    have_sticker = input('Vous avez sticker suivi?(Y/N): ')
    have_sticker = have_sticker == 'Y'
    print(calcul_cost_letter(type_letter, weight_letter, to_zone, have_sticker))

"""
Affranchissement postal
Type de colis(verte, prioritaire, ecopli, outre-mer): verte
Poids du colis: 112
Vers zone(1,2): 1
Vous avez sticker suivi?(Y/N): N
4.6
"""