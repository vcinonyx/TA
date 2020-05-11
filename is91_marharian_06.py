class Median:

    def __init__(self):
        self.H_high = Heap('min')  # створюється об'єкт min_heap
        self.H_low = Heap('max')  # створюється об'єкт max_heap

    def add(self, num):
        if self.H_low.size() != 0 and num <= self.H_low.top():  # якщо число менше за значення вершини(i=0) h_low
            self.H_low.insert(num)  # вставляємо елемент в h_low
        else:
            self.H_high.insert(num)  # вставляємо елемент в h_high

        right_size = self.H_high.size()  # розмір масива H_high
        left_size = self.H_low.size()  # розмір масива H_low

        if right_size - left_size > 1:  # якщо  кількість елементів в h_high на 2 більше за h_low
            self.H_low.insert(self.H_high.pop())  # видаляється вершина h_high та вставляється в H_low
        elif left_size > right_size:  # якщо кількість елементів в h_low > h_high, то вставляємо вершину H-low в h_igh
            self.H_high.insert(self.H_low.pop())

    def find_median(self):

        right_size = self.H_high.size()  # розмір масива H_high
        left_size = self.H_low.size()  # розмір масива H_low

        if right_size == left_size:
            return self.H_low.top(), self.H_high.top()  # якщо довжина парне число то повертаємо 2 значення
        else:
            return self.H_high.top(), ''  # повертаємо медіану


class Heap:

    def __init__(self, order):
        self.items = []  # масив де зберігаються елементи min/max_heap
        self.order = order  # ключ, який дорівнює min/max

    def size(self):
        return len(self.items)  # повертається довжина масива

    def insert(self, item):  # вставка елемента
        self.items.append(item)  # вставка елемента в кінець масива
        self.check_parent(len(self.items) - 1)  # перевірка умови max/min heap для вставленого елемента

    def top(self):
        return self.items[0]  # вершина піраміди

    def pop(self):
        temp_item = self.items[0]  # зберігаємо в змінну темп перший елемент масиву
        self.items[0], self.items[-1] = self.items[-1], self.items[0]  # змінюємо місцями останній і перший елементи
        self.items.pop()  # видаляємо останній елемент
        self.heapify(0)  # виконання процедури heapify починаючи з вершини
        return temp_item

    def check_parent(self, i):
        if i == 0:  # якщо розмір масива = 0  перевірка не виконується
            return
        parent = (i + 1) // 2 - 1  # індекс батьківського вузла

        if self.order == 'min':  # сортування для min_heap
            if self.items[parent] > self.items[i]:  # якщо батьківський більше за дочірній  то міняємо місцями
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
                self.check_parent(parent)  # якщо виконалась умова рекурсивний виклик
        else:  # сортування для max_heap
            if self.items[parent] < self.items[i]:  # якщо батьківський менше за дочірній  то міняємо місцями
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
                self.check_parent(parent)  # якщо виокуналась умова для max_heap

    def heapify(self, i):
        n = len(self.items)  # довжина поточного масива
        left = i * 2 + 1  # індекс лівого дочірнього елемента
        right = i * 2 + 2  # індекс правго дочірнього елемента
        parent = i  # індекс батьківського вузла
        if self.order == 'min':  # min_heap
            if left < n and self.items[parent] > self.items[left]:  # якщо батьківський більше за лівий дочірній
                parent = left  # заміна індекса parent
            if right < n and self.items[parent] > self.items[right]:  # якщо батьківський більше за правий дочірній
                parent = right  # змінюється індекс parent
            if parent != i:  # якщо виконалась одна з умов, то елементи мінаються місцями
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
                self.heapify(parent)  # після заміни викликається функція heapify зі зміненим індексом

        if self.order == 'max':  # max_heap
            if left < n and self.items[parent] < self.items[left]:  # якщо батьківський більше за лівий дочірній
                parent = left  # новий індекс для parent = left
            if right < n and self.items[parent] < self.items[right]:  # якщо батьківський менше за правий дочірній
                parent = right  # новий індекс для parent = right
            if parent != i:  # якщо виконалась одна з умов, зазначених вище
                self.items[parent], self.items[i] = self.items[i], self.items[parent]  # змінюємо батьківський дочірній
                self.heapify(parent)  # повторення здійсненої операції з новим індексом


for i in range(1, 21, 1):

    A = Median()  # створюється об'єкт який складається з min_heap та max_heap

    if i < 10:
        temp = "0"
    else:
        temp = ""
    if i < 6:
        N = "10"
    elif i < 11:
        N = "100"
    elif i < 16:
        N = "1000"
    else:
        N = "10000"

    input_file = open("input_" + temp + str(i) + "_" + N + ".txt")
    output_file = open("is91_marharian_06_output_" + temp + str(i) + "_" + N + ".txt", "w")
    arr = []
    for line in input_file.readlines():
        arr.append(int(line))  # додаємо в масив елементи з текстового файлу
    arr.pop(0)  # видалення нульового елемента
    array = list(arr)  # копіюємо зчитаний масив
    for index in range(len(arr)):  # послідовно для кожного з елементів масива
        A.add(arr[index])  # додаємо елемент
        output_file.writelines(str('{0[0]} {0[1]}'.format(A.find_median())) + '\n')
    input_file.close()
    output_file.close()
