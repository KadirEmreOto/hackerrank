from itertools import combinations

def o(n):
    a = 0
    while n:
        a += n & 1
        n >>= 1
    return a

def ones(n):
  if n < 4294967296: return o(n)
  n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
  n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
  n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
  n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
  n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
  n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This last & isn't strictly necessary.
  return n

n = int(raw_input())
a = map(int, raw_input().split())

if not any(a):
    print 67108864
    quit()

oo = 0
answer = 64
for i in xrange(1, n+1):
    for subset in combinations(a, i):
        s = [subset[0]]
        for it in subset[1:]:
            found = False
            for j in xrange(len(s)):
                if s[j] & it:
                    s[j] |= it
                    found = True
                    break
            if not found:
                s.append(it)

        answer += 64
        for j in s:
            oo += 1
            answer -= ones(j) - 1
print answer

