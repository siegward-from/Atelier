def discriminant(a: float, b: float, c: float) -> float:
    return (b ** 2) - (4 * a * c)


def racine_unique(a: float, b: float) -> float:
    try:
        return -b / (2 * a)
    except ZeroDivisionError:
        return 0


def racine_double(a: float, b: float, delta: float, num: int) -> float:
    try:
        return (-b + (delta, -delta)[num-1] ** (1/2)) / (2 * a)
    except ZeroDivisionError:
        return 0


def str_equation(a: float, b: float, c: float) -> str:
    return f'{a}x2 + {b}x + {c} = 0'


def solution_equation(a: float, b: float, c: float) -> str:
    delta = discriminant(a, b, c)
    if delta < 0:
        return f"Solution de l'équation {str_equation(a, b, c)} \n" \
               f"Pas de racine réelle \n"
    elif delta == 0:
        return f"Solution de l'équation {str_equation(a, b, c)} \n" \
               f"Racine unique : x = {racine_unique(a, b)} \n"
    else:
        x1 = racine_double(a, b, delta, 1)
        x2 = racine_double(a, b, delta, 2)
        return f"Solution de l'équation {str_equation(a, b, c)} \n" \
               f"Deux racines : \n" \
               f"x1 = {x1} \n" \
               f"x2 = {x2} \n"


def test_solutions() -> None:
    print(f'Delta < 0, ({str_equation(2, 1, 2)}): \n'
          f'{solution_equation(2, 1, 2)}')
    print(f'Delta == 0, ({str_equation(1, 2, 1)}): \n'
          f'{solution_equation(1, 2, 1)}')
    print(f'Delta > 0, ({str_equation(1, 5, 4)}): \n'
          f'{solution_equation(1, 5, 4)}')


if __name__ == '__main__':
    test_solutions()
