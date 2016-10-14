
n = int(raw_input())
a = map(int, raw_input().split())

i = 0
answer = 0

while i != (n-1):
    if i + 1 == (n-1) or i + 2 == (n-1): i = n-1
    elif not a[i + 2]: i += 2
    else: i += 1

    answer += 1

print answer

