
def BinarySearch(array, value):
    left = 0
    right = len(array) - 1
    answer = -1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == value:
            return mid
        if array[mid] < value:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

a = []
n = int(raw_input())

for i in xrange(n):
    t, f = map(int, raw_input().split())
    a.append((t-f, t+f))

a.sort()

temp = [a[0][1]]
for i in xrange(1, n):
    if a[i][1] < temp[-1]:
        temp.append(a[i][1])

    else:
        pos = BinarySearch(temp, a[i][1])
        temp[pos] = a[i][1]

print len(temp)

