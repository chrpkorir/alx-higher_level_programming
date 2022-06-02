#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end='')  # abs() return absolute value of number
    return (abs(number) % 10)
