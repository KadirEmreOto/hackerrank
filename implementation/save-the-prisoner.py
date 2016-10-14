# Enter your code here. Read input from STDIN. Print output to STDOUT

for t in xrange(int(raw_input())):
    n, m, s = map(int, raw_input().split())
    r = (m % n + s - 1) % n
    if not r: r = n
    print r

