counter = 0

def QuickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

def MedianQuickSort(A, p, r):
    if p < r:
        q = MedianPartition(A, p, r)
        MedianQuickSort(A, p, q-1)
        MedianQuickSort(A, q+1, r)

def MedianPartition(A, p, r):
    if r - p > 2:
        med = Median(A[p], A[(p+r)//2], A[r])
        index = A.index(med)
        A[index], A[r] = A[r], A[index]
    return partition(A, p, r)

def partition(A, p, r):
    i = p-1
    x = A[r]
    global counter
    for j in range(p, r):
        counter +=1
        if A[j] <  x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def GetValues(filename):
    bin  = "/Users/vcinonyx/PycharmProjects/algorithms_t/input_TA/" #path to the input txt files on your pc
    file = open(bin + filename +".txt")
    values = []
    for line in file.readlines():
        values.append(int(line))
    values.pop(0);
    return values

def Median(a, b, c):
   return sorted([a, b, c])[1]

for i in range(1, 21, 1):
    if i <= 10:
        if i <= 5:
            filename = "input_0" + str(i)+"_10"
        else:
            filename = "input_0" + str(i) + "_100"
            if i == 10:
                filename = "input_"+str(i)+"_100"
    else:
        if i <= 15:
            filename = "input_" + str(i) + "_1000"
        else:
            filename = "input_" + str(i) + "_10000"

    data = GetValues(filename)
    array = list(data)
    print("unsorted array:", array)
    QuickSort(array,0, len(array)-1)
    print("sorted array:", array)
    print("quick sort counter = ", counter)
    array = list(data)
    quick_counter = counter
    counter = 0
    MedianQuickSort(array, 0, len(array)-1)
    print("median sort counter = ", counter, "\n\n")
    median_counter = counter
    counter = 0
    file_name = "is91_marharian_04_"+"output_"+str(i)+"_"+str(len(data)) + ".txt"
    output = open(file_name, "w+")
    output.write(str(quick_counter) + "  " + str(median_counter))
    output.close()
