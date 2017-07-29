
for _ in xrange(int(raw_input())):
    a, b = map(lambda x: int(x) ** 0.5, raw_input().split())
    print int(b) - int(a) + a.is_integer()
    
