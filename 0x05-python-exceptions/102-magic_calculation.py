#!/usr/bin/python3

result = 0
def magic_calculation(a, b):
    for i in range(1, 3):
        try:
            if i > a:
                raise NameError("Too far")
        except NameError as e:
            print(e)

        finally:

        result += (a**b) / i

        print(a, i, result)

        result = b + a

