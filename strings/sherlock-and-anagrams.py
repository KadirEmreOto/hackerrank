
from math import factorial
from collections import Counter

comb = lambda n, r: factorial(n) / (factorial(n-r)*factorial(r))

T = int(raw_input())

for _ in xrange(T):
    string = raw_input()
    length = len(string)
    array = []

    for i in xrange(length):
        subarray = []
        for j in xrange(length - i):
            sub = string[j:j+i+1]
            subarray.append(str(sorted(sub)))
        array.append(subarray)

    answer = 0
    for subarray in array:
        counter = Counter(subarray)

        for i in counter:
            if counter[i] > 1:
                answer += comb(counter[i], 2)
    print answer



