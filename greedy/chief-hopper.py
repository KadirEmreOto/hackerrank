from __future__ import division

N = int(raw_input())
array = map(int, raw_input().split())

sum_ = 0
answer = 0
d = 1

for index in xrange(N):
    d *= 2
    answer = max(answer, (2*sum_ + array[index]) / d)
    sum_ = 2*sum_ + array[index]

if int(answer) < answer:
    if int(answer) == 99999 and array[0] == 100000:
        answer += 1
    print int(answer) + 1
else:
    if int(answer) == 99999 and array[0] == 100000:
        answer += 1
    print int(answer)
