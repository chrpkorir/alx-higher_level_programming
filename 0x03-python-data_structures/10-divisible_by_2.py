#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy_list = []
    for num in my_list:
        if num % 2 == 0:
            cpy_list.append(True)
        else:
            cpy_list.append(False)
    return cpy_list
