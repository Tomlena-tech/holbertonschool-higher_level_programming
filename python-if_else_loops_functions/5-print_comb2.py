#!/usr/bin/python3
for number in range(0,99):
    if number <10:
        print("0{:d}".format(number), end=", ")
    else: print("{:d}".format(number), end=", ")
print("99")
