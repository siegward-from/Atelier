def contain_zero(num: int) -> bool:
    return '0' in str(num)

def separer(l: list) -> list:
    return [e for e in l if e < 0] + [e for e in l if contain_zero(e)] + [e for e in l if e > 0 and not contain_zero(e)]

l = [-1, -2, -9, 0, 1, 4, 7, 10, 20]
print(separer(l))

# 14 00