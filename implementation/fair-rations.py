
N = int(raw_input())
array = map(int, raw_input().split())

i = 0
answer = 0
while i < N-1:
    if not array[i] & 1:
        i += 1
        continue

    else:
        answer += 1
        array[i+1] += 1
    i += 1

if array[-1] & 1: print 'NO'
else: print answer * 2

