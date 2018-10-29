"""
    Here I study recursion in programming.
"""

# sum function with for-loop
def sum(list):
    sum_result = 0
    for item in list:
        sum_result += item
    return sum_result

# sum function with recursion
def sum_rec(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_rec(list[1:])

# counter of items in list with recursion 
def count_rec(list):
    if list == []:
        return 0
    else:
        return 1 + count_rec(list[1:])

if __name__ == '__main__':
    testin_l = [1, 24, 6, 234, 340, 3, 0, 2]
    print("testing:", 1 + 24 + 6 + 234 + 340 + 3 + 0 + 2)
    print(sum(testin_l))
    print(sum_rec(testin_l))
    print("In list", count_rec(testin_l), "elements.")