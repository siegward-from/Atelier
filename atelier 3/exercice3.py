import random


# question 1
def places_lettres(char: str, mot: str) -> list[int]:
    """ :return: Liste des positions de caractère dans mot """
    return [i for i in range(len(mot)) if mot[i] == char]


def output_str(mot: str, lpos: list[int]) -> str:
    """ :return Le mot avec underscore au lieu des lettres dont la position n'est pas dans la liste """
    return ''.join(mot[i] if i in lpos else '_' for i in range(len(mot)))


def chose_level() -> str:
    """ :return: Niveau de difficulté entré par l'utilisateur """
    level = None
    while level not in ('easy', 'normal', 'hard'):
        level = input('niveau de diffculté(easy, normal, hard): ')
    return level


def chose_word(words_list: list[str], level: str) -> str:
    """ :return Mot aléatoire de la liste qui correspond au niveau de difficulté """
    match level:
        case 'easy':
            return select_word(build_dict(words_list), random.randint(5, 6))
        case 'normal':
            return select_word(build_dict(words_list), random.randint(7, 8))
        case 'hard':
            return select_word(build_dict(words_list), random.randint(9, 10))


def run_game():
    """ Jeu de pendu """
    level = chose_level()
    words_list = ['paris', 'londres', 'madrid', 'berlin', 'new-york']
    errors = 0
    positions = []
    word = chose_word(words_list, level)
    print_list = ["|---] ",
                  "| O ",
                  "| T ",
                  "|/ \\ ",
                  "|____"
                  ]

    while errors < 5:
        letter = input("lettre: ")
        position = places_lettres(letter, word)
        if not position:
            errors += 1
            if errors == 5:
                print('Vous avez perdu')
        else:
            positions += position

        guess = output_str(word, positions)
        print_list[-1] = f'|{guess}'
        for i in print_list[errors:]:
            print(f'{i}')
        print(f'erreurs: {errors}\n')
        if guess == word:
            print("Vous avez gagné")
            errors = 5


# question 4
def build_list(filename: str) -> list[str]:
    """ Prend en paramètre un nom de fichier et construit automatiquement la liste des mots """
    with open(filename) as file_:
        return [line[:-1] for line in file_]


# question 5
def build_dict(lst: list[str]) -> dict[int:str]:
    """ Prend en paramètre une liste de mots et construit automatiquement le dictionnaire """
    return {
        i: [e for e in lst if len(e) == i]
        for i in range(1, max([len(e) for e in lst]) + 1)
        if [e for e in lst if len(e) == i]
    }


def select_word(sorted_words: dict[int: str], word_len: int) -> str:
    """
    Prend en paramètre le dictionnaire précédemment créé et
    retourne un mot choisi au hasard dans la liste des mots de taille word_len
    """
    try:
        list_ = sorted_words[word_len]
        return list_[random.randint(0, len(list_) - 1)]
    except (ValueError, KeyError):
        return ''


if __name__ == '__main__':
    run_game()
