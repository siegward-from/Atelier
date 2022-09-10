def annee_bissextile(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def test_annee() -> None:
    print('1977 % 4 != 0:', annee_bissextile(1977))
    print('1978 % 4 == 0 and 1978 % 100 != 0:', annee_bissextile(1980))
    print('2100 % 100 == 0 and 2100 % 400 != 0:', annee_bissextile(2100))
    print('2400 % 400 == 0:', annee_bissextile(2400))


if __name__ == '__main__':
    test_annee()
