#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for value  in my_list[:x]:
        try:
            print("{:d}".format(value), end="")
                except ValueError:
                continue
                except TypeError:
                continue
