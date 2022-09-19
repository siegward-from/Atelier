def mots_n_lettres(list_mot: list[str], n: int) -> list[str]:
    """ :return La liste des mots contenant exactement n lettres """
    return [word for word in list_mot if len(word) == n]


def commence_par(mot: str, prefixe: str) -> bool:
    """ :return True si l'argument mot commence par prefixe et False sinon """
    return mot[:len(prefixe)] == prefixe


def finit_par(mot: str, suffixe: str) -> bool:
    """ :return True si l'argument mot se termine par suffixe et False sinon """
    return mot[-len(suffixe):] == suffixe


def finissent_par(list_mot: list[str], suffixe: str) -> list[str]:
    """ :return La liste des mots présents dans la liste lst_mot qui se terminent par suffixe """
    return [word for word in list_mot if finit_par(word, suffixe)]


def commencent_par(list_mot: list[str], prefixe: str) -> list[str]:
    """ :return La liste des mots présents dans la liste lst_mot qui commencent par prefixe """
    return [word for word in list_mot if commence_par(word, prefixe)]


def liste_mots(list_mot: list[str], prefixe: str, suffixe: str, n: int) -> list[str]:
    """ :return La liste des mots présents dans lst_mot
                qui commencent par prefixe, se terminent par suffixe et
                contiennent exactement n lettres """
    return finissent_par(commencent_par(mots_n_lettres(list_mot, n), prefixe), suffixe)


def dictionnaire(fichier: str) -> list[str]:
    """ :return La liste des mots présents dans le fichier """
    with open(fichier) as file_:
        return [line[:-1] for line in file_]


# tests
def test_mots_n_letters():
    assert mots_n_lettres(['a', 'b', 'ab', 'bc', 'abc', 'bac', 'acb'], 3) == ['abc', 'bac', 'acb']
    assert mots_n_lettres(['a', 'b', 'ab', 'bc', 'abc', 'bac', 'acb'], 0) == []
    assert mots_n_lettres([], 3) == []
    assert mots_n_lettres([], 0) == []


def test_commence_par():
    assert commence_par('python', 'p')
    assert commence_par('python', 'py')
    assert not commence_par('python', 'on')
    assert not commence_par('python', '123')


def test_finit_par():
    assert finit_par('python', 'n')
    assert finit_par('python', 'on')
    assert not finit_par('python', 'py')
    assert not finit_par('python', '123')


def test_finissent_par():
    assert finissent_par(['abc', 'qwe', 'zxc', 'a1c'], 'c') == ['abc', 'zxc', 'a1c']
    assert finissent_par(['abc', 'qwe', 'zxc', 'a1c'], 'e') == ['qwe']
    assert finissent_par(['abc', 'qwe', 'zxc', 'a1c'], 't') == []
    assert finissent_par([], 'a') == []


def test_commencent_par():
    assert commencent_par(['abc', 'qwe', 'zxc', 'a1c'], 'a') == ['abc', 'a1c']
    assert commencent_par(['abc', 'qwe', 'zxc', 'a1c'], 'z') == ['zxc']
    assert commencent_par(['abc', 'qwe', 'zxc', 'a1c'], 't') == []
    assert commencent_par([], 'a') == []


def test_liste_mots():
    assert liste_mots(['abc', 'qwe', 'zxc', 'a1c'], 'a', 'c', 3) == ['abc', 'a1c']
    assert liste_mots(['abc', 'qwe', 'zxc', 'a1c'], 'z', 'c', 3) == ['zxc']
    assert liste_mots(['abc', 'qwe', 'zxc', 'a1c'], 't', 'c', 3) == []
    assert liste_mots(['abc', 'qwe', 'zxc', 'a1c'], 'a', 't', 3) == []
    assert liste_mots(['abc', 'qwe', 'zxc', 'a1c'], 'a', 'c', 1) == []


if __name__ == '__main__':
    test_mots_n_letters()
    test_commence_par()
    test_finit_par()
    test_commencent_par()
    test_finissent_par()
    test_liste_mots()
