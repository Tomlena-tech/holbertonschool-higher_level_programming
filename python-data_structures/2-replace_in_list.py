#!/usr/bin/python3
def replace_in_list (my_list, idx, new_element):
    for i in range(len(my_list)):
        if idx == -1 or idx >=(len(my_list)):
            return my_list
        if i == idx:
            my_list[i] = new_element
            return my_list
