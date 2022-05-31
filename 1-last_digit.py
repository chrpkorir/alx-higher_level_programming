#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if number > 5 and last_digit > 5:
    print("Last digit of {} is {} ".format(number, last_digit))
elif number == 0 and last_digit == 0:
     print("Last digit of {} is {} ".format(number, last_digit))
elif number < 6 and not 0 and last_digit < 6 and not 0:
     print("Last digit of {} is {} ".format(number, last_digit))
