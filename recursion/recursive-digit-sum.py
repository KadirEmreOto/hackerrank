# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum_digit(number):
    ans = 0
    for i in number:
        ans += int(i)
    return str(ans)

def super_digit(n):
    if len(n) == 1:
        return n
    return super_digit(sum_digit(n))

n, k = raw_input().split()
k = int(k)

n = sum_digit(n)
n = sum_digit(str(int(n) * k))
print super_digit(n)



