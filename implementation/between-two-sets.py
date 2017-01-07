
def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

a = lcm(*a)
b = gcd(*b)
if b % a != 0: print 0; quit()
    
c = 0
i = 1
while a * i <= b:
    c += (b % (a*i) == 0)
    i += 1
print c


