#!/usr/bin/python3

def roman_to_int(roman_string):

    if roman_string == "" or roman_string == None:
        return 0

    roman_num =  {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    temp = roman_num[roman_string[0]]
    sum_roman = 0
    
    if len(roman_string) == 1:
        return temp

    else:
        for value in range(1, len(roman_string)):

            if roman_string[value] in roman_num:

                if temp >= roman_num[roman_string[value]]:
                    sum_roman += temp
                else:
                    sum_roman -= temp

                temp = roman_num[roman_string[value]]
            else:
                print("wrong input")
                return (0)

        sum_roman += temp
        return (sum_roman)
