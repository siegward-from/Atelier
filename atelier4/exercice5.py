import random
import time
import matplotlib.pyplot as plt
import numpy as np
import exercice2 as ex2
import exercice4 as ex4


def perf_mix(function1: callable, function2: callable, list_: list, numbre_execution: int, els: int = None) -> tuple:
    """ Permet de calculer le temps d’exécution moyen desdeux fonctions de mélange """
    start_time1 = time.perf_counter()
    if els is None:
        for i in range(numbre_execution):
            function1(list_)
    else:
        for i in range(numbre_execution):
            function1(list_, els)
    end_time1 = time.perf_counter()
    start_time2 = time.perf_counter()
    if els is None:
        for i in range(numbre_execution):
            function2(list_)
    else:
        for i in range(numbre_execution):
            function2(list_, els)
    end_time2 = time.perf_counter()
    return end_time1 - start_time1, end_time2 - start_time2


def test_mix_list(function1: callable, function2: callable, list_: list, numbre_execution: int, els: int = None) -> None:
    y_value_list1 = []
    y_value_list2 = []
    len_list = len(list_)
    for i in range(len_list - 5, len_list):
        time_of_function1, time_of_function2 = perf_mix(function1, function2, list_[:i+1], numbre_execution, els)
        y_value_list1.append(time_of_function1)
        y_value_list2.append(time_of_function2)
    x_axis_list = np.arange(5, 10, 1)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, np.array(y_value_list1), 'bo-', label='first function')
    ax.plot(x_axis_list, np.array(y_value_list2), 'r*-', label='second function')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


list_to_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_mix_list(ex2.mix_list, random.shuffle, list_to_test, 1000)
test_mix_list(ex4.extract_elements_list, random.sample, list_to_test, 1000, 2)
