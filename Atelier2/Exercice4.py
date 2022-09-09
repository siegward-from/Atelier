from Exercice1 import val_max
from Exercice2 import nb_occurrences
import matplotlib.pyplot as plt

# Question 1
# 1)
def histo(f):
    return [nb_occurrences(f, i) for i in range(val_max(f) + 1)]


F = [6, 5, 6, 8, 4, 2, 1, 5]
print(histo(F), '\n')

# 2)
def est_injective(f):
    l = histo(f)
    more_one = lambda x: x > 1
    return all([not more_one(e) for e in l])

F1 = [6, 5, 6, 7, 4, 2, 1, 5]
F2 = [3, 0, 6, 7, 4, 2, 1, 5]
print(est_injective(F1))
print(est_injective(F2), '\n')

# 3)
def est_surjective(f):
    l = histo(f)
    less_one = lambda x: x < 1
    return all([not less_one(e) for e in l])

print(est_surjective(F1))
print(est_surjective(F2), '\n')

# question 2
def positions(l, e):
    result = []
    for i in range(len(l)):
        if l[i] >= e:
            result.append(i)
    return result

def affiche_histo(f):
    print('TEST HISTOGRAMME\n')
    print(f'F = {f}\n')
    print('HISTOGRAMME')
    l = histo(f)
    value2 = val_max(f)
    for i in range(val_max(l), 0, -1):
        line = '   ' * value2
        for p in positions(l, i):
            line = line[:p * 3 + 1] + '#' + line[p * 3 + 2:]
        print(line)
    print('|-|' * (value2 + 1))
    for i in range(10):
        print(f' {i} ', end='')
    for i in range(10, 16):
        print(f' {i}', end='')

F = [1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
affiche_histo(F)
#15 40
# question 3 15 50
def affiche_histo1(f):
    plt.hist(f)
    plt.title('Histogramme avec MatPlotLib')
    plt.show()

affiche_histo1(F)
#15 50

