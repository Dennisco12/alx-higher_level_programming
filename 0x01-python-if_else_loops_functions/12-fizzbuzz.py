#!/usr/bin/python3
def fizzbuzz():
    """A code that prints the fizzbuzz"""
    for m in range(1, 101):
        if (m % 3 == 0 and m % 15 != 0):
            print("Fizz", end=' ')
        elif (m % 5 == 0 and m % 15 != 0):
            print("Buzz", end=' ')
        elif m % 15 == 0:
            print("FizzBuzz", end=' ')
        else:
            print("{}".format(m), end=' ')
