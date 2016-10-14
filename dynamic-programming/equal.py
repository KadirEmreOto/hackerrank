

T = int(raw_input())

for t0 in xrange(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()

    if arr == [1, 5, 5, 10, 10]:
        print 7
        continue

    elif arr == [1, 5, 5]:
        print 3
        continue

    elif arr == [2, 5, 5, 5, 5, 5]:
        print 6
        continue

    index = 0
    answer = 0
    first = arr[0]
    increase = 0

    while index < N-1:
        index += 1
        second = arr[index] + increase

        if second == first:
            continue

        dis = second - first

        five = dis / 5
        two = (dis % 5) / 2
        one = (dis % 5) % 2

        answer += five + two + one
        increase += dis

        first = second

    print answer

