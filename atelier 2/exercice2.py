def position1(l: list, e: int) -> int:
    for i in range(len(l)):
        if l[i] == e:
            return i
    return -1


def position2(l: list, e: int) -> int:
    pos = 0
    while l:
        if l.pop(0) == e:
            return pos
        else:
            pos += 1
    return -1


def nb_occurrences(l: list, e: int) -> int:
    result = 0
    for e1 in l:
        if e1 == e:
            result += 1
    return result


def est_triee1(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def est_triee2(l: list) -> bool:
    if len(l) != 0:
        value = l.pop(0)
        while l:
            next_value = l.pop(0)
            if value > next_value:
                return False
            value = next_value
    return True


def position_tri(l: list, e: int) -> int:
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == e:
            return mid
        elif l[mid] > e:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def a_repetitions(l: list) -> bool:
    for i in range(len(l)-1, 0, -1):
        if l[i] in l[:i]:
            return True
    return False


def test1(function: callable((list, int)), text):
    print(text)
    print('test [], 0:', function([], 0))
    print('test [1, 2, 3], 0:', function([1, 2, 3], 0))
    print('test [0, 1, 2], 0:', function([0, 1, 2], 0))
    print('test [0, 0, 1], 0:', function([0, 0, 1], 0), '\n')


def test2(function: callable(list), text):
    print(text)
    print('test []:', function([]))
    print('test [1, 2, 3]:', function([1, 2, 3]))
    print('test [3, 2, 1]:', function([3, 2, 1]))
    print('test [1, 1, 2]:', function([1, 1, 1]))
    print('test [2, 2, 1]:', function([2, 2, 1]), '\n')


if __name__ == '__main__':
    test1(position1, 'test position1')
    test1(position2, 'test position2')
    test1(position_tri, 'test position_tri')
    test1(nb_occurrences, 'test nb_occurrences')
    test2(est_triee1, 'test est_triee1')
    test2(est_triee2, 'test est_triee2')
    test2(a_repetitions, 'test a_repetitions')
