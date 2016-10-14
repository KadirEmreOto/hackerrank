
from collections import Counter

N = int(raw_input())
A = map(int, raw_input().split())
B = map(int, raw_input().split())

C = Counter(A)
D = Counter(B)

answer = 0

for i in C:
    if i in D:
        answer += min(C[i], D[i])

if C == D: answer -= 1
else: answer += 1

print answer
