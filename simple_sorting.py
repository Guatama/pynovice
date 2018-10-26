# simple sorting and function for smallest element

def smallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0
    for index in range(1, len(arr)):
        if arr[index] < smallest:
            smallest = arr[index]
            smallest_index = index
    return smallest_index

def simpleSort(arr):
    new_arr = []
    for item in range(len(arr)):
        smallest = smallestIndex(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

list1 = [34, 4, 1, 0, 3345, 345, 3253, 10, 234, 23, 53, 70, 2, 3, 1, 34, 5, 10]
print("List without sorting: ", list1)
print("List with sorting: ", simpleSort(list1))

def findSecondIndex(arr):

    new_arr = simpleSort(arr)
    arr_return = []
    index = 0
    second_index = 0
    for index in new_arr:
        if index == new_arr[index + 1]
            second_index = index
    return second_index

print(findSecondIndex(list1))