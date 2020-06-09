import numpy as np
from numpy import sqrt
from math import inf
from os import startfile


def find_path(X, Y):
    way = []  # список, що зберігає індекси пройдених міст в порядку обходу
    DistanceMatrix = np.zeros([n, n])  # створення матриці відстаней розміром N x N
    for i in range(n):  # для кожної комірки матриці відстаней
        for j in range(n):
            if i != j:
                DistanceMatrix[i, j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)  # заповнення матриці відстаней
            else:
                DistanceMatrix[i, j] = inf  # заповнення головної діагоналі матриці

    way.append(0)  # додаємо до шляху індекс початкової вершини, в нашому випадку завжди 0

    for i in range(1, n):  # починаючи з другого міста
        s = []  # масив для збереження відстаней з міста
        for j in range(n):
            s.append(DistanceMatrix[way[i - 1], j])  # обчислення відстаней всіх можливих шляхів з даної вершини
        way.append(s.index(min(s)))  # додаємо до шляху вершину, відстань до якої - найкоротша
        for j in range(i):
            DistanceMatrix[way[i], way[j]] = inf  # позначаємо  пройдені вершинин як нескінченність, тобто недоступні
    S = sum([sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2) for i in range(n - 1)]) \
        + sqrt((X[way[n - 1]] - X[way[0]]) ** 2 + (Y[way[n - 1]] - Y[way[0]]) ** 2)  # обчислення суми відстаней
    return way, S


def readfile(filename):
    input_file = open(filename)
    x = []  # x - координати точок
    y = []  # у - координати точок
    m = []  # проміжний масив для збереження зчитаних елементів
    for line in input_file.readlines():  # порядково
        m = line.split()  # m - масив з елементів у файлі типу str
        if len(m) > 1:  # якщо рядок містить 2 елементи, то
            x.append(int(m[0]))  # перший елемент рядку координата х
            y.append(int(m[1]))  # другий елемент рядку координата у
    input_file.close()
    return x, y


def save(filename, _path, result):
    output = open(filename, 'w')
    output.write(str(result.__round__(1)) + "\n")
    for node in _path:
        output.write(str(node) + ' ')
    output.close()


if __name__ == '__main__':
    for i in range(1, 2):
        X, Y = readfile("input_0" + str(i) + ".txt")  # заповнення масивів координат
        n = len(X)  # кількість вершин
        path, sums = find_path(X, Y)  # знаходимо шлях та суму
        save("is91_marharian_output_0" + str(i) + ".txt", path, sums)