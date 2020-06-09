

def backpack(maxWeight, number_of_items, w, v):
    matrix = [[0] * (maxWeight + 1)]  # створюємо матрицю з (об'єм мішка + 1) стовпців та з (n-предметів + 1) рядків
    # нульовий рядок матриці заповнений нулями
    for i in range(number_of_items):  # послідовно для кожного предмету
        matrix.append(matrix[i].copy())  # копіюємо до поточного рядка матриці значення з попереднього
        print(f"предмет: {i+1}\tw[{i+1}] = {w[i]}  value[{i+1}] = {v[i]}")
        for k in range(w[i], maxWeight + 1):  # починаючи з ваги поточного предмета й до максимальної можливої
            matrix[i + 1][k] = max(matrix[i][k], matrix[i][k - w[i]] + v[i])  # обираємо найбільше можливе значення
        print(matrix[i+1])
        print()

    return matrix[number_of_items][maxWeight]  # повертаємо результат


def save_doc(_filename, SUM):
    output = open(_filename, 'w')
    output.write(str(SUM))
    output.close()


def readfile(_filename):
    input_file = open(_filename)
    v = []  # вартість
    w = []  # вага
    for line in input_file.readlines():  # порядково
        m = line.split()  # m - масив з елементів у файлі типу str
        v.append(int(m[0]))
        w.append(int(m[1]))
    input_file.close()
    return v, w


def main():
    inputs = [5, 10]
    for _ in inputs:
        values, weights = readfile(f"input_{_}.txt")
        max_weight = values[0]
        values.pop(0)
        weights.pop(0)
        items = len(values)
        result = (backpack(max_weight, items, weights, values))
        save_doc(f"marharian_10_output_{_}.txt", result)
        print(result)


if __name__ == '__main__':
    main()
