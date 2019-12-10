#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = (-number) % 10
else:
    last_digit = number % 10

print("Last digit of {} is {} and is".format(number, last_digit), end=" ")
if last_digit > 5:
    print('and is greater than 5'.format(number, last_digit))
if last_digit == 0:
    print('and is 0'.format(number, last_digit))
if (last_digit < 6) and (last_digit != 0):
    print('and not 0'.format(number, last_digit))
