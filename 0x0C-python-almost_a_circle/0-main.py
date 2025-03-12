#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    b6 = Base(None)
    print(b6.id)

    b7 = Base("jk7")
    print(b7.id)

    b8 = Base()
    b8.id = 14
    print(b8.id)

    b9 = Base(jk7)
    print(b7.id)
