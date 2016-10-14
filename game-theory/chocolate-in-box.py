
def digits(number):
    if not number: return 0
    return 1 + digits(number>>1)

N = int(raw_input())
arr = map(int, raw_input().split())

top = reduce(lambda x, y: x^y, arr)

d = digits(top)
res = 0

if top:
    for item in arr:
        if item >> (d-1) & 1:
            res += 1

print res

