#!/usr/bin/python3
def safe_print_division(a, b):
    if a is None or b is None:
        return None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
