#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        print("Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0) or number,
              end=" ")
