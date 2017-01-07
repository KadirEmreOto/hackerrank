
n, t = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()

i = 0
j = 0
answer = 0

while i < n:
    answer += 1
    while j < n and a[j] - a[i] <= t: j += 1

    if j == n: break

    i = j - 1

    while j < n and a[j] - a[i] <= t: j += 1

    i = j

print answer


