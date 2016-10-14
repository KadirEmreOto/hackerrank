#!/usr/bin/py
import operator
def lonelyinteger(a):
    answer = reduce(operator.xor, a)
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

