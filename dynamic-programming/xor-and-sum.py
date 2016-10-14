# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input(), 2)
b = int(raw_input(), 2)

answer = 0
for i in xrange(314160):
    answer += a ^ (b << i)
print answer % (10**9 + 7)
