def message_imc(weight: int, height: float) -> float:
    try:
        return weight / height ** 2
    except ZeroDivisionError:
        return 0


def test_imc() -> None:
    print('test negative height(1, -1):', message_imc(1, -1))
    print('test positive height(1, 1):', message_imc(1, 1))
    print('test zero height(1, 0):', message_imc(1, 0))


if __name__ == '__main__':
    test_imc()
