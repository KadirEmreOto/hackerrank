
def valid(t):
    return (t[0] + t[1]) > t[2] and (t[1]-t[0]) < t[2]

n = int(raw_input())
a = map(int, raw_input().split())
a.sort()

answer = [-1]
for i in xrange(n-3, -1, -1):
    if valid(a[i:i+3]):
        answer = a[i:i+3]
        break

print ' '.join(map(str, answer))

