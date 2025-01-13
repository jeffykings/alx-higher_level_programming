#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists.

    Args:
        my_list_1: the first list which will be the numerator
        my_list_2: The second list which will be the denominator
        list_length: the length of the new list

    """
    new_list = []

    for i in range(list_length):
        try:
            value =  my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            Value = 0
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            new_list.append(value)

    return (new_list)
