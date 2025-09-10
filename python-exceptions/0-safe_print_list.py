#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or x < 0:
        print()
        return 0
    count = 0
    if x > len(my_list):
        x =len(my_list)
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
    
    