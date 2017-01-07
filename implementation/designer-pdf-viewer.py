
h = map(int, raw_input().split())
word = raw_input()
l = 0
for i in word:
    l = max(l, h[ord(i) - ord('a')])
print len(word) * l
