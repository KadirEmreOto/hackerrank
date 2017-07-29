
n = int(raw_input())
a = [raw_input() for i in xrange(n)]
a.sort(key=lambda x: (len(x), x))
print '\n'.join(a)
