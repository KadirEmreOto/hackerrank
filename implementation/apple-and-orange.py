#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

a1 = 0
a2 = 0
for i in apple: a1 += (s-a <= i <= t-a)
for i in orange: a2 += (s-b <= i <= t-b)
print a1
print a2


