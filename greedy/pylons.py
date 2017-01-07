
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

i = 0
answer = 0
k -= 1
while i < n:
    check = False
    for j in xrange(min(n-1, i+k), i, -1):
        if a[j] == 1:
            answer += 1
            i = j + k + 1
            check = True
            break

    if not check and a[i] == 1:
        answer += 1
        i += k + 1

    elif not check:
        for j in xrange(i-1, i-k-1, -1):
            if j >= 0 and a[j] == 1:
                answer += 1
                i = j + k + 1
                check = True
                break

        if not check:
            print -1
            quit()

print answer

