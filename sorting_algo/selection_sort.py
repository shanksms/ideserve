def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        index = find_smallest(arr)
        new_arr.append(arr.pop(index))
    return new_arr

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

if __name__ == '__main__':
    print(selection_sort([3, 6, 2, 9, 8]))
