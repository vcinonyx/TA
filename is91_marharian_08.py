import os

results = []

class Node:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

def print_sum_path(root, path, k):
    # empty node
    if not root:
        return

    # add current node to the path
    path.append(root.root)

    # check if there's any k sum path
    # in the left sub-tree.
    print_sum_path(root.left, path, k)

    # check if there's any k sum path
    # in the right sub-tree.
    print_sum_path(root.right, path, k)

    # check if there's any k sum path that
    # terminates at this node
    # Traverse the entire path as
    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]
        # If path sum is k, print the path
        if f == k:
            print_vector(path, j)
            # Remove the current element
    # from the path
    path.pop(-1)

def print_vector(v, i):
    global results
    output = ""
    for j in range(i, len(v)-1):
        output += (str(v[j])+"+")
    output += str(v[-1])
    results.append(output)

def sum_path(root, k):
    path = []
    print_sum_path(root, path, k)


def in_order(root, mas):
    if root is None:
        return
    in_order(root.left, mas)
    mas.append(root.root)
    in_order(root.right, mas)


def bst(root, arr): #
    if root is None:
        return
    bst(root.left, arr)
    root.root = (arr[0])
    arr.pop(0)
    bst(root.right, arr)


def arr_to_tree(root, dataArray, index):  # create array
    if dataArray[index] == 0:
        return index
    if dataArray[index + 1] != 0:
        root.left = Node(dataArray[index+1])
    index = arr_to_tree(root.left, dataArray, index+1)
    if dataArray[index + 1] != 0:
        root.right = Node(dataArray[index+1])
    index = arr_to_tree(root.right, dataArray, index+1)
    return index

def read_file(name):
    input_file = open(name)
    read_array = []
    m = []
    for line in input_file.readlines():
        m = line.split()
    read_array = [int(m[i]) for i in range(len(m))]
    input_file.close()
    return read_array

def save_file(name):
    global results
    filename = name.replace('input_', 'is91_marharian_08_output_')
    output = open(filename, 'w')
    for string in results:
        output.writelines(string + "\n")
    os.startfile(filename)


if __name__ == '__main__':
    file_name = input("Введіть назву файла: ")
    arr = read_file(file_name)
    root = Node(arr[0])
    arr_to_tree(root, arr, 0)
    array = []
    in_order(root, array)  # returns an in order array
    array.sort()
    bst(root, array)  # convert binary tree to bst
    sum_path(root, int(input("Введіть суму: ")))
    save_file(file_name)

