import random
import time
import matplotlib.pyplot as plt
import numpy as np


def stupid_sort(list_: list[float | int]) -> None:
    while sorted(list_) != list_:
        random.shuffle(list_)


def tri_insertion(list_: list[float | int]) -> list[float | int]:
    result = list_[:]
    for i in range(len(result)):
        x = result[i]
        j = i
        while j > 0 and result[j - 1] > x:
            result[j] = result[j - 1]
            j -= 1
        result[j] = x
    return result


def tri_selection(list_: list[float | int]) -> list[float | int]:
    result = list_[:]
    length = len(result)
    for i in range(length - 2):
        min = i
        for j in range(i + 1, length - 1):
            if result[j] < result[min]:
                min = j
        if min != i:
            result[i], result[min] = result[min], result[i]
    return result


def tri_a_bulles(list_: list[float | int]) -> list[float | int]:
    result = list_[:]
    length = len(result)
    for i in range(length - 1, 0, -1):
        triee = True
        for j in range(i - 1):
            if list_[j + 1] < list_[j]:
                list_[j + 1], list_[j] = list_[j], list_[j + 1]
                triee = False
        if triee:
            return result
    return result


def tri_fusion(list_: list[float | int]) -> list[float | int]:
    if len(list_) < 2:
        return list_
    element = list_[0]
    less = [el for el in list_ if el < element]
    more = [el for el in list_ if el > element]
    return tri_fusion(less) + [element] + tri_fusion(more)


def radix_sort(list_: list[tuple]) -> list[tuple]:
    if len(list_) < 2:
        return list_
    element = list_[0]
    less = [el for el in list_[1:] if el[1] < element[1]]
    more = [el for el in list_[1:] if el[1] >= element[1]]
    return radix_sort(less) + [element] + radix_sort(more)


def radix_order_sort(list_: list[float | int], order: int):
    list_with_order = [(el, int(str(el)[-order]) if len(str(el)) > order else 0) for el in list_]
    sorted_list_with_order = radix_sort(list_with_order)
    return [el[0] for el in sorted_list_with_order]


def perf_sort_list(function: callable, list_1: list[float | int], numbre_execution: int) -> tuple:
    list_2, list_3 = list_1, list_1
    list_2.reverse()
    random.shuffle(list_3)
    start_time1 = time.perf_counter()
    for i in range(numbre_execution):
        function(list_1)
        function(list_2)
        function(list_3)
    end_time1 = time.perf_counter()
    start_time2 = time.perf_counter()
    for i in range(numbre_execution):
        sorted(list_1)
        sorted(list_2)
        sorted(list_3)
    end_time2 = time.perf_counter()
    return end_time1 - start_time1, end_time2 - start_time2


def test_sort_list(function_name: str, function: callable, list_: list[float | int], numbre_execution: int) -> None:
    y_value_list1 = []
    y_value_list2 = []
    len_list = len(list_)
    for i in range(len_list - 5, len_list):
        time_of_function1, time_of_function2 = perf_sort_list(function, list_[:i + 1], numbre_execution)
        y_value_list1.append(time_of_function1)
        y_value_list2.append(time_of_function2)
    x_axis_list = np.arange(5, 10, 1)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, np.array(y_value_list1), 'bo-', label=f'{function_name}')
    ax.plot(x_axis_list, np.array(y_value_list2), 'r*-', label='sorted()')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


list_to_test = [i for i in range(5)]
test_sort_list('stupid_sort()', stupid_sort, list_to_test, 10)
list_to_test = [i for i in range(5)]
test_sort_list('tri_insertion()', tri_insertion, list_to_test, 100)
test_sort_list('tri_selection()', tri_selection, list_to_test, 100)
test_sort_list('tri_a_bulles()', tri_a_bulles, list_to_test, 100)
test_sort_list('tri_fusion()', tri_fusion, list_to_test, 100)

