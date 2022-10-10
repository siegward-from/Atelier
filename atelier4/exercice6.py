from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import time


def sort_list(list_: list[float | int]) -> list[float | int]:
    if len(list_) < 2:
        return list_
    element = list_[0]
    less = [el for el in list_ if el < element]
    more = [el for el in list_ if el > element]
    return sort_list(less) + [element] + sort_list(more)


def perf_sort_list(list_1: list[float | int], numbre_execution: int) -> tuple:
    list_2, list_3 = list_1, list_1
    list_2.reverse()
    shuffle(list_3)
    start_time1 = time.perf_counter()
    for i in range(numbre_execution):
        sort_list(list_1)
        sort_list(list_2)
        sort_list(list_3)
    end_time1 = time.perf_counter()
    start_time2 = time.perf_counter()
    for i in range(numbre_execution):
        sorted(list_1)
        sorted(list_2)
        sorted(list_3)
    end_time2 = time.perf_counter()
    return end_time1 - start_time1, end_time2 - start_time2


def test_sort_list(list_: list[float | int], numbre_execution: int) -> None:
    y_value_list1 = []
    y_value_list2 = []
    len_list = len(list_)
    for i in range(len_list - 5, len_list):
        time_of_function1, time_of_function2 = perf_sort_list(list_[:i + 1], numbre_execution)
        y_value_list1.append(time_of_function1)
        y_value_list2.append(time_of_function2)
    x_axis_list = np.arange(5, 10, 1)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, np.array(y_value_list1), 'bo-', label='first function')
    ax.plot(x_axis_list, np.array(y_value_list2), 'r*-', label='second function')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


list_to_test = [i for i in range(10)]
test_sort_list(list_to_test, 100)
