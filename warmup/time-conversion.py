#!/bin/python

time = raw_input().strip()
t = map(int, time[:-2].split(':'))

if time[-2:] == 'PM':
    t[0] += 12
    if t[0] == 24:
        t[0] = 12

if time[-2:] == 'AM':
    if t[0] == 12:
        t[0] = 0
    


    
t = map(str, t)
print ':'.join(map(lambda i:i.zfill(2), t))

