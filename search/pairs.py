#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    a.sort()
    
    answer = 0
    for i in xrange(1, len(a)):
        for j in xrange(i-1, -1, -1):
            diff = a[i] - a[j]
            if diff > k:
                break
            elif diff == k:
                answer += 1
                break

    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)

