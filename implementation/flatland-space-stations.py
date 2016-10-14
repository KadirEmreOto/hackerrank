
n, m = map(int, raw_input().split())
array = map(int, raw_input().split())
array.sort()

answer = max((n-1 -array[-1]), (array[0]))
for i in xrange(m-1):
    a = (array[i+1] - array[i]) / 2
    if answer < a:
        answer = a

print answer

