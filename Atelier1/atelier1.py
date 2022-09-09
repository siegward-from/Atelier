from random import randint
import datetime

# exercice 1
def message_imc(weight: int, height: float) -> float:
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

def test_annee(list_year):
    for year in list_year:
        print(f'{year}: {annee_bissextile(year)}')

# test_annee([1902, 1904, 1920, 1933, 2000])

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

def test_solutions(list_coefs) -> None:
    for cf in list_coefs:
        print(solution_equation(cf))

# test_solutions([(1, 2, 1), (2, 4, 1), (2, 1, 2)])

# exercice 4
def date_est_valide(annee: int, mois: int, jour: int) -> bool:
    if annee_bissextile(annee):
        if mois == 2:
            if jour > 29:
                return False
    else:
        if mois == 2:
            if jour > 28:
                return False
    if mois % 2 == 0:
        if jour > 30:
            return False
    else:
        if jour > 31:
            return False
    if mois > 12 or annee > 2022:
        return False
    return True

def saisie_date_naissance() -> datetime:
    date = input('Date(AAAA-MM-JJ): ')
    annee, mois, jour = int(date[:4]), int(date[5:7]), int(date[8:10])
    if date_est_valide(annee, mois, jour):
        return datetime.datetime(annee, mois, jour)

def age(date_naissance: datetime) -> int:
    return datetime.datetime.today().year - date_naissance.year

def est_majeur(date_naissance: datetime) -> bool:
    return age(date_naissance) >= 18

def test_acces() -> None:
    date = saisie_date_naissance()
    if est_majeur(date):
        print(f"Bonjour, vous avez {age(date)} ans, Accès autorisé")
    else:
        print(f"Désolé, vous avez {age(date)} ans, Accès interdit")

def test_functions(iters) -> None:
    for i in range(iters):
        date = datetime.datetime(randint(1950, 2022), randint(1, 12), randint(1, 30))
        print(date, age(date), est_majeur(date))

test_functions(10)