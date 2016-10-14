
n, k = map(int, raw_input().split())
numb = bytearray(raw_input())
temp = set([])

for i in xrange(n / 2 + 1):
    if numb[i] != numb[-i-1]:
        if not k: print -1; quit()
        numb[i] = numb[-i-1] = max(numb[i], numb[-i-1])
        temp.add(i)

        k -= 1

i = 0
while k and i < (n / 2 + 1):
    if numb[i] != ord('9'):
        if k >= 2 and not i in temp:
            numb[i] = numb[-i-1] = ord('9')
            k -= 2

        elif i in temp or i == (n-i-1):
            numb[i] = numb[-i-1] = ord('9')
            k -= 1

    i += 1

print numb

