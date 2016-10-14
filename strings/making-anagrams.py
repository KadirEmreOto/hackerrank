# Enter your code here. Read input from STDIN. Print output to STDOUT

a = raw_input()
b = raw_input()

answer = 0

for i in range(97, 123):
    answer += abs(a.count(chr(i)) - b.count(chr(i)))
print answer
