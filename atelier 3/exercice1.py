def full_name(str_arg: str) -> str:
    """ :return  str_arg avec le nom en majuscule et le prénom avec la première lettre seulement en majuscule"""
    list_arg = str_arg.split()
    return list_arg[0].upper() + ' ' + list_arg[1].lower().capitalize()


def is_mail(str_arg: str) -> (int, int):
    """
    Verifier si mail est valide
    Conditions:
    Mail doit contenir @ et . après @,
    Le corps ne doit pas être vide et le premier et le dernier caractère du corps doivent être des lettres
    Le domaine avant . ne doit pas être vide et le domaine après . ne doit pas être plus court que 2 caractères
    :param str_arg: mail adresse
    :return: Première valeur est la validation de l'adresse (1: mail valide, 0: mail non valide)
             Second valeur est le type d'erreur (1: corps, 2: il manque l'@, 3: domaine, 4: il manque le .)
    """
    if '@' not in str_arg:
        return 0, 2
    elif '.' not in str_arg.split('@')[1]:
        return 0, 4
    corps, domaine = str_arg.split('@')
    if len(corps) == 0 or not corps[0].isalpha() or not corps[-1].isalpha():
        return 0, 1
    first_part_domaine, last_part_domaine = domaine.split('.')
    if not first_part_domaine or len(last_part_domaine) < 2:
        return 0, 3

    return 1, 0


def test_full_name():
    assert full_name('bisgambiglia paul') == 'BISGAMBIGLIA Paul'
    assert full_name('BISGAMBIGLIA PAUL') == 'BISGAMBIGLIA Paul'


def test_is_mail():
    assert is_mail('bisgambiglia_paul@univ-corse.fr') == (1, 0)
    assert is_mail('bisgambiglia_paulOuniv-corse.fr') == (0, 2)
    assert is_mail('bisgambiglia_paul@univ-corsePOINTfr') == (0, 4)
    assert is_mail('@univ-corse.fr') == (0, 1)
    assert is_mail('bisgambiglia_paul@.fr') == (0, 3)


if __name__ == '__main__':
    test_full_name()
    test_is_mail()
