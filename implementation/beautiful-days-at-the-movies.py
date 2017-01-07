
def reverse(number):
    answer = 0
    while number:
        number, rem = divmod(number, 10)
        answer += rem
        answer *= 10
    return answer / 10

i, j, k = map(int, raw_input().split())
answer = 0

for i in xrange(i, j+1):
    if not abs(i - reverse(i)) % k:
        answer += 1
        
print answer
