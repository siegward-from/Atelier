import datetime
from exercice2 import annee_bissextile


def date_est_valide(annee: int, mois: int, jour: int) -> bool:
    if mois == 2:
        if annee_bissextile(annee):
            if jour > 29:
                return False
        else:
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


def test_functions() -> None:
    print(f"(1980-01-01): \n"
          f"Age: {age(datetime.datetime(1980, 1, 1))} \n"
          f"Est majeur: {est_majeur(datetime.datetime(1980, 1, 1))} \n")
    print(f"(2007-01-01): \n"
          f"Age: {age(datetime.datetime(2007, 1, 1))} \n"
          f"Est majeur: {est_majeur(datetime.datetime(2007, 1, 1))}")


test_functions()
