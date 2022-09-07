from random import  randint

# exercice 1
def message_imc(weight: int, height: int) -> float:
    return weight / height ** 2

def test_imc(iter: int) -> None:
    for i in range(iter):
        weight = randint(60, 90)
        height = randint(160, 190) / 100
        print(weight, height, message_imc(weight, height))

test_imc(10)
print()

# exercice 2
def  annee_bissextile(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# exercice 3
def discriminant(a: float, b: float, c: float) -> float:
    return (b ** 2) - (4 * a * c)

def racine_unique(a: float, b: float) -> float:
    return -b / (2 * a)

def racine_double(a: float, b: float, delta: float, num: int) -> float:
    if num == 1:
        return (-b + delta ** (1/2)) / (2 * a)
    elif num == 2:
        return (-b - delta ** (1/2)) / (2 * a)

def str_equation(a: float, b: float, c: float) -> str:
    return f'{a}x2 + {b}x + {c} = 0'

def solution_equation(a: float, b: float, c: float) -> str:
    delta = discriminant(a, b, c)
    if delta < 0:
        return f"Solution de l'équation {str_equation(a, b, c)} \nPas de racine réelle"
    elif delta == 0:
        return f"Solution de l'équation {str_equation(a, b, c)} \nRacine unique : x = {racine_unique(a, b)}"
    else:
        x1 = racine_double(a, b, delta, 1)
        x2 = racine_double(a, b, delta, 2)
        return f"Solution de l'équation {str_equation(a, b, c)} \nDeux racines : \nx1 = {x1}\nx2 = {x2}"

def test_solutions() -> None:
    while True:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        if a == 0 and b == 0 and c == 0:
            break
        print(solution_equation(a, b, c))

test_solutions()

# exercice 4
def date_est_valide(jour, mois, annee):
