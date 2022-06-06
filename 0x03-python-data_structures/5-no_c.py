#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    i = 0
    while i < len(str_list):
        if str_list[i] in ['c', 'C']:
            str_list.pop(i)
        else:
            i += 1
    return "".join(str_list)
