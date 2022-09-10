from exercice1 import val_max
from exercice2 import nb_occurrences
import matplotlib.pyplot as plt


# Question 1
# 1)
def histo(f: list[int]) -> list[int]:
    return [nb_occurrences(f, i) for i in range(val_max(f) + 1)]


F = [6, 5, 6, 8, 4, 2, 1, 5]
print('test histo()')
print(f'test {F}:', histo(F), '\n')


# 2)
def est_injective(f: list[int]) -> bool:
    return all([not e > 1 for e in histo(f)])


F1 = [6, 5, 6, 7, 4, 2, 1, 5]
F2 = [3, 0, 6, 7, 4, 2, 1, 5]
print('test est_injective()')
print(f'test {F1}', est_injective(F1))
print(f'test {F2}', est_injective(F2), '\n')


# 3)
def est_surjective(f: list[int]) -> bool:
    return all([not e < 1 for e in histo(f)])


print('test est_surjective()')
print(f'test {F1}', est_surjective(F1))
print(f'test {F2}', est_surjective(F2), '\n')


# question 2
def affiche_histo(f: list[int]) -> None:
    def positions(l: list[int], e: int) -> list[int]:
        result = []
        for i in range(len(l)):
            if l[i] >= e:
                result.append(i)
        return result
    print('TEST HISTOGRAMME\n')
    print(f'F = {f}\n')
    print('HISTOGRAMME')
    l = histo(f)
    value = val_max(f)
    # afficher tous les caractères #
    for i in range(val_max(l), 0, -1):
        line = '   ' * value
        for p in positions(l, i):
            line = line[:p * 3 + 1] + '#' + line[p * 3 + 2:]
        print(line)

    print('|-|' * (value + 1))
    for i in range(10):
        print(f' {i} ', end='')
    for i in range(10, 16):
        print(f' {i}', end='')


F = [1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
affiche_histo(F)


# 15 40
# question 3 15 50
def affiche_histo1(f: list[int]) -> None:
    plt.hist(f)
    plt.title('Histogramme avec MatPlotLib')
    plt.show()


affiche_histo1(F)
