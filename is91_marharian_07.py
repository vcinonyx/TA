collision = 0  # змінна для підрахунку колізій

def hashing_multiply(KEY, hash_table):  # хеш-функція за методом множення
    mod = KEY * 0.6180339887  # в
    result = int(len(hash_table) * (mod - int(mod)))  # обчислюємо за формулою
    return result  # повертаємо індекс

def hashing_divide(KEY, hash_table):  # хеш-функція за методом ділення
    result = KEY % len(hash_table)  # за формулою визначаємо
    return result  # повертаємо індекс

def insert(hash_table, key, value, hashing_method):  # заповнення хеш таблиці елементами з масива
    global collision  # лічильник колізій
    if hashing_method == 'ділення':  # викликається метод ділення
        hash_key = hashing_divide(key, hash_table)  # за допомогою функції hashing визначається ключ(індекс) в хеш
        hash_table[hash_key].append(value)  # вставка елемента за отриманим ключем(індексом)
    else:   # якщо викликається метод множення
        hash_key = hashing_multiply(key, hash_table)  # за допомогою функції hashing визначається ключ(індекс)
        hash_table[hash_key].append(value)  # вставка елемента в хеш таблицю за отриманим ключем(індексом)


    #  обчислення колізій під час вставки елементів
    if len(hash_table[hash_key]) > 1:  # якщо кількість елементів в комірці таблиці > 1,
        collision += 1  # додаємо 1 до лічильника колізій
        for i in range(len(hash_table[hash_key])-1):  #
            if hash_table[hash_key][i] == value:  # якщо елементи комірки однакові, то колізія не враховується
                collision -= 1
                break  # припиняємо цикл

def hash_search(hash_table, elem, hashing_method):  # метод пошуку елемента в хеш таблиці, elem = sum - x,
    if hashing_method == "ділення":  # якщо обрано метод ділення
        sub_array = hash_table[hashing_divide(elem, hash_table)]  # sub_array - масив,що містить
        # елементи певної комірки хеш таблиці
    else:  # якщо обрано метод множення
        sub_array = hash_table[hashing_multiply(elem, hash_table)]
    if not sub_array:  # якщо sub_array масив пустий
        return False  # вертаємо False як знак, що елемент не знайдений
    else:  # якщо sub_array не пустий
        for i in range(len(sub_array)):  # проходимо по всіх індексах масиву sub_array
            if sub_array[i] == elem:  # якщо знайшли елемент
                return elem  # повертаємо його
    return False  # якщо не знайшли - повертаємо False, як знак, що елемент не знайдений

def division_hash(A, m):  # Хеш-таблиця на основі ланцюгів із використанням хеш-функції за методом ділення.
    output_file = open("is91_marharian_07_output_"+ str(len(A)) + "_2" + ".txt", "w")   # назва вихідного файла
    hash_table = [[] for _ in range(3*len(A))] # хеш таблиця створена за допомогою вкладених спискиів
    for key in A: # для кожного елемента масива А
        insert(hash_table, key, key, "ділення")  # вставляється елемент масиву А в хеш таблицю за методом ділення
    output_file.writelines(str(collision) + "\n")  # запис кількості колізій у файл
    for i in range(len(m)):  # для кожної суми з масива
        flag = False   # булева змінна для виведення 0, 0 в файл, якщо для даної суми не існує відповідних елементів А
        for j in range(len(A)):   # для кожного елемента масива А
            if hash_search(hash_table, m[i]-A[j], "ділення"):  # якщо  в хеш таблиці знайдені відповідні значення
                output_file.writelines((str(A[j]) + " " + str(m[i]-A[j]) + "\n"))  # записуємо в файл дані числа
                flag = True   # якщо існують числа які в сумі дорівнюють даній сумі
                break  # якщо знайшли чилса - припиняємо цикл
        if flag == False:  # якщо флаг = false
            output_file.writelines("0  0 \n")  # якщо для даної суми не знайшлось елементів
    output_file.close()  # закриваємо файл


def multiply_hash(A, m):  # функція на основі ланцюгів із використанням хеш-функції з методом множення.
    output_file = open("is91_marharian_07_output_" + str(len(A)) + "_1" + ".txt", "w")  # назва вихідного файла
    hash_table = [[] for _ in range(3*len(A))]  # хеш таблиця створена за допомогою вкладених спискиів
    for key in A:   # для кожного елемента масива А
        insert(hash_table, key, key, "множення")  # вставляється елемент масиву А в хеш таблицю за методом множення
    output_file.writelines(str(collision) + "\n")  # запис кількості колізій у файл
    for i in range(len(m)):  # для кожного елемента масива сум
        flag = False  # булева змінна для виведення 0, 0 в файл, якщо для даної суми не існує відповідних елементів А
        for j in range(len(A)):  # для кожного елемента масива А
            if hash_search(hash_table, m[i] - A[j], "множення"):  # якщо  в хеш таблиці знайдені відповідні значення
                output_file.writelines((str(A[j]) + " " + str(m[i] - A[j]) + "\n"))  # записуємо в файл дані числа
                flag = True  # якщо існують числа які в сумі дорівнюють даній сумі
                break
        if flag == False: # якщо для даної суми не знайшлось елементів
            output_file.writelines("0  0 \n")  # виконується запис в файлі
    output_file.close()  # закриваємо файл


def readfile(name):  # функція заповнення масивів з файлу
        A_length = 0  # довжина масива А
        M_length = 0  # довжина масива сум
        input_file = open("input_" + str(10**name) + ".txt")  # файл звідки зчитуються значення
        arr = []  # масив всіх елементів з файлу
        for line in input_file.readlines():  # Перетворення даних вхідного файла у массив
            m = line.split()  # масив значень
            if len(m) > 1:   # в першій стрічці 2 елементи, де 1 - довжина А, 2 - довжина м
                A_length = int(m[0])
                M_length = int(m[1])
            else:
                arr.append(int(m[0]))  # для решти рядків
        input_file.close()  # закриваємо файл
        A = []  # масив значень
        M = []  # масив сум
        for i in range(A_length):
            A.append(int(arr[i]))   # заповнення масива А
        for i in range(A_length, len(arr)):
            M.append(int(arr[i]))  # заповнення масива М
        return A, M  # повертаємо значення масивів


plus = 1
for i in range(3):  # для кожного з вхідних файлів
    A, m = readfile(i+plus)  # запис файлу у масиви A та m
    plus += 1
    division_hash(A, m)  # Хеш-таблиця на основі ланцюгів із використанням хеш-функції за методом ділення
    collision = 0  # обнуляємо лічильник для подальшого використання
    multiply_hash(A, m)  # Хеш-таблиця на основі ланцюгів із використанням хеш-функції за методом множення
