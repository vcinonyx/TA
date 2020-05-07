import random
import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(mass):
    counter = 0
    for i in range(len(mass) - 1):
        swapped = False
        for j in range(len(mass) - 1):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
                swapped = True
            counter += 1
        if not swapped:
            break
    return counter

def improved_bub_sort(mass):
    counter = 0
    for i in range(len(mass) - 1):
        swapped = False
        for j in range(len(mass) - i - 1):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
                swapped = True
            counter += 1
        if not swapped:
            break
    return counter


def insertion_sort(mass):
    counter = 0
    for i in range(1, len(mass)):
        key = mass[i]
        j = i - 1
        while j >= 0 and mass[j] > key:
            mass[j + 1] = mass[j]
            j -= 1
            counter += 1
        mass[j + 1] = key
        counter += 1
    return counter


def create_array(length, key):
    if key == "best":
        mass = [x for x in range(length)]
        return mass
    elif key == "worst":
        mass = [x for x in reversed(range(length))]
        return mass
    else:
        mass = [x for x in range(length)]
        random.shuffle(mass)
        return mass


def create_graphics(graph_data):
    color = ['r', 'g', 'b']
    lines = [':', '--', '-']
    line_type = 0
    for i in graph_data:
        index = 0
        for j in graph_data[i]:
            plt.plot(list(graph_data[i][j].keys()), list(graph_data[i][j].values()), color[index] + lines[line_type],
                     label=i+" case "+j+" sort ")
            index += 1
        line_type += 1
    plt.ylabel("COUNTER")
    plt.xlabel("ARRAY LENGTH")
    plt.grid(which="major")
    plt.legend()
    plt.show()


graphData = {'best': {'Bubble': {}, 'Improved Bubble': {}, 'Insertion': {}},
             'worst': {'Bubble': {}, 'Improved Bubble': {}, 'Insertion': {}},
             'random': {'Bubble': {}, 'Improved Bubble': {}, 'Insertion': {}}}

types = ["best", "worst", "random"]
size = [x for x in range(1000)]

for N in size:

    for sort_type in types:
        array = create_array(N, sort_type)

        bubble_Array = list(array)
        bubbleCounter = bubble_sort(bubble_Array)
        graphData[sort_type]['Bubble'][N] = bubbleCounter

        improved_Bubble_Array = list(array)
        improvedBubbleCounter = improved_bub_sort(improved_Bubble_Array)
        graphData[sort_type]['Improved Bubble'][N] = improvedBubbleCounter

        insertion_Array = list(array)
        insertionCounter = insertion_sort(insertion_Array)
        graphData[sort_type]['Insertion'][N] = insertionCounter

create_graphics(graphData)
