def calcul_cost(type: str, weight: int, zone: int, sticker: bool) -> float:
    """
    Calcule affranchissement postal
    :param type: str(verte, prioritaire, ecopli, outre-mer)
    :param weight: int
    :param zone: int(1, 2)
    :param sticker: bool
    :return: float montan d'affranchissement postal
    """
    summe = 0
    final_weight = weight // 10
    if weight % 10 != 0:
        final_weight += 1

    if sticker:
        summe += 0.5

    if type == 'verte':
        tarif = {20: 1.16, 100: 2.32, 250: 4, 500: 6, 1000: 7.5, 3000: 10.5}
        keys_tarif = list(tarif.keys())
        for key in keys_tarif:
            if weight <= key:
                summe += tarif[key]
                break
        if zone == 1:
            summe += final_weight * 0.05
        elif zone == 2:
            summe += final_weight * 0.11

    elif type == 'prioritaire':
        tarif = {20: 1.43, 100: 2.86, 250: 5.26, 500: 7.89, 3000: 11.44}
        keys_tarif = list(tarif.keys())
        for key in keys_tarif:
            if weight <= key:
                summe += tarif[key]
                break
        if zone == 1:
            summe += final_weight * 0.05
        elif zone == 2:
            summe += final_weight * 0.11

    elif type == 'ecopli':
        tarif = {20: 1.14, 100: 2.28, 250: 3.92}
        keys_tarif = list(tarif.keys())
        for key in keys_tarif:
            if weight <= key:
                summe += tarif[key]
                break
        if zone == 1:
            summe += final_weight * 0.02
        elif zone == 2:
            summe += final_weight * 0.05

    elif type == 'outre-mer':
        tarif = {0.5: 8.35, 1: 11.20, 2: 14.10, 5: 23.65, 10: 37.50, 15: 75.85, 30: 87.40}
        keys_tarif = list(tarif.keys())
        for key in keys_tarif:
            if weight <= key:
                summe += tarif[key]
                break

    return round(summe, 2)


print('Affranchissement postal')
type = input('Type de colis(verte, prioritaire, ecopli, outre-mer): ')
weight = int(input('Poids du colis: '))
zone = int(input('Vers zone(1, 2): '))
sticker = input('Vous avez sticker suivi?(Y/N): ')
sticker = sticker == 'Y'
print(calcul_cost(type, weight, zone, sticker))

"""
Affranchissement postal
Type de colis(verte, prioritaire, ecopli, outre-mer): verte
Poids du colis: 112
Vers zone(1,2): 1
Vous avez sticker suivi?(Y/N): N
4.6
"""