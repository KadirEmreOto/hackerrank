#!/bin/python

import sys
import string

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

temp = ''

letter = {
    True : string.ascii_lowercase,
    False: string.ascii_uppercase
}


for i in s:
    if i in letter[i.islower()]:
        index = letter[i.islower()].index(i)
        index += k
        i = letter[i.islower()][index % len(letter[i.islower()])]
    temp += i
    
print temp
        

