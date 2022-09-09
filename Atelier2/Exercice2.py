def position1(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return i
    return -1

def position2(l, e):
    pos = 0
    while l:
        if l.pop(0) == e:
            return pos
        else:
            pos += 1
    return -1

def nb_occurrences(l, e):
    result = 0
    for e1 in l:
        if e1 == e:
            result += 1
    return result

def est_triee(l):
    return all([l[i] < l[i+1] for i in range(len(l)-1)])

def position_tre(l, e):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        e1 = l[mid]
        if e1 == e:
            return mid
        elif e1 > e:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def a_repetitions(l):
    for i in range(len(l)-1, 0, -1):
        if l[i] in l[:i]:
            return True
    return False

# 11 30