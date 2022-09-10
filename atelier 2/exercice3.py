def contain_zero(num: int) -> bool:
    return '0' in str(num)


def separer(l: list) -> list:
    return [e for e in l if e < 0] + \
           [e for e in l if contain_zero(e) and e >= 0] + \
           [e for e in l if e > 0 and not contain_zero(e)]


if __name__ == '__main__':
    print('test [-1, 1, -5, 5, -10, 10, 0]:', separer([-10, -5, -1, 0, 1, 5, 10]))
