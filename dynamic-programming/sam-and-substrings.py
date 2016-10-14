
mod = (10**9 + 7)
answer = 0
string = raw_input()
lenght = len(string)

array = [0]
for i in xrange(lenght):
    array.append((10*array[-1] + 1) % mod)


for i in xrange(lenght):
    number = int(string[i])
    answer += (i + 1) * number * array[-i-1]

print answer % (10**9 + 7)

