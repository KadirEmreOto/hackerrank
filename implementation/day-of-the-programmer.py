#!/bin/python

import sys

def solve(year):
    if year == 1918:
        s = "26.09.1918"

    elif year % 4 == 0 and year % 100 != 0 or year == 1700 or year == 1800 or year == 1900 or year % 400 == 0:
        s = "12.09." + str(year)

    else:
        s = "13.09." + str(year)
        
    return s

year = int(raw_input().strip())
result = solve(year)
print(result)

