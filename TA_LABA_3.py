import random
import numpy as np
import matplotlib.pyplot as plt
from time import time

def insertion_sort(input_mass):
    mass = input_mass
    for i in range(1, len(mass)):
        key = mass[i]
        j = i - 1
        while j >= 0 and mass[j] > key:
            mass[j + 1] = mass[j]
            j -= 1
        mass[j + 1] = key

def merge_sort(seq, p, r):
    if r - p <= 1:
        return

    q = (r + p) // 2
    merge_sort(seq, p, q)
    merge_sort(seq, q, r)
    merge(seq, p, q, r)


def merge(seq, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1 - 1):
        L[i] = seq[p + i]

    for j in range(0, n2 - 1):
        R[j] = seq[q + j]

    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(p - 1, r - 1):
        # print i,j,p,r
        if L[i] <= R[j]:
            seq[k] = L[i]
            i = i + 1
        else:
            seq[k] = R[j]
            j = j + 1
    return seq


def create_array(length):
    mass = [x for x in range(length)]
    random.shuffle(mass)
    return mass


def test_insertion(array):
    start = time()
    mass = list(array)
    insertion_sort(mass)
    end = time()
    return end - start


def test_merge(array):
    start = time()
    mass = list(array)
    merge_sort(mass, 0, len(mass))
    end = time()
    return end - start


def create_graphics(graph_data):
    color = ['r', 'b']
    lines = ['-', '*']
    line_type = 0
    for i in graph_data:
        index = 0
        for j in graph_data[i]:
            plt.plot(list(graph_data[i][j].keys()), list(graph_data[i][j].values()), color[index] + lines[line_type],
                     label=i + " case " + j + " sort ")
            index += 1
        line_type += 1
    plt.ylabel("RUNTIME")
    plt.xlabel("ARRAY LENGTH")
    plt.grid(which="major")
    plt.legend()
    plt.show()


repeats = 1000
types = ["random"]
graph_data = {'random': {'insertion': {}, 'merge': {}}}


for n in range(2, 150, 1):
    print("\nDATA SIZE: ", n)
    data = create_array(n)
    mergeTime = 0
    insertionTime = 0
    for m in range(repeats):
        merge_array = list(data)
        mergeTime += test_merge(merge_array)
        graph_data['random']['merge'][n] = mergeTime
        print("mergeTime =", mergeTime, "\n")

        insertion_array = list(data)
        insertionTime += test_insertion(insertion_array)
        graph_data['random']['insertion'][n] = insertionTime
        print("insertionTime =", insertionTime, "\n")

    graph_data['random']['merge'][n] = (graph_data['random']['merge'][n])/repeats
    graph_data['random']['insertion'][n] = (graph_data['random']['insertion'][n])/repeats

create_graphics(graph_data)
