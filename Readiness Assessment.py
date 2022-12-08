# Given two lists of numbers, write a procedure that returns a list of the element-wise sum of the number in those two lists. In the following, no imports should be used.

def add_two_lists(a, b):
    sum_list = []
    for i in range(len(a)):
        sum_list.append(a[i] + b[i])
    return sum_list

