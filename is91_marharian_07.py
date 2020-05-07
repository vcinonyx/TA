
def hashing_f(key):
    mod = key * 0.618033
    result = int(len(hash_table)* (mod - int(mod)))
    return result


def insert(hash_table, key, value):
    hash_key = hashing_f(key)
    hash_table[hash_key].append(value)

def hash_search(hash_table, elem):  # метод пошуку елемента в хеш таблиці
    sub_array = hash_table[hashing_f(elem)]  # subArray - масив, який містить елементи певної "комірки" хеш таблиці
    if not sub_array:  # якщо subArray масив пустий
        return False  # вертаємо False як знак, що елемент не знайдений
    else:  # якщо subArray не пустий
        for i in range(len(sub_array)):  # проходимо по всіх індексах масиву subArray
            if sub_array[i] == elem:  # якщо знайшли елемент
                return elem  # повертаємо його
    return False  # якщо не знайшли - повертаємо False, як знак, що елемент не знайдений


A = [40, 12, 79, 35, 43, 52, 83, 66, 89, 79]
hash_table = [[] for i in range(3*len(A))]
m = [88, 87, 126, 78, 122]
for i in A:
    insert(hash_table, i, i)
print(hash_table)
flag = False
for i in range(len(m)):
    for j in range(len(A)):
        if hash_search(hash_table,m[i]-A[j]) != False:
            print(A[j], " ",m[i]-A[j])
            flag = True
            break
    if flag == False:
        print(0," ",0)

