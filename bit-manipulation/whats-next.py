#-*- coding: UTF-8 -*-

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    array = map(int, raw_input().split())

    if N == 1:
        if array[0] == 1:
            array = [1, 1]
        else:
            array[0] -= 1
            array = [1, 1, array[0]]

    elif N == 2:
        if array[0] != 1:
            array.append(1)
            array = array[::-1]
            array[-1] -= 1
            array[-2] += 1
        else:
            array[-1] += 1

    elif N % 2: # odd: 10101
        i = N-1

        if array[i] == 1 and array[i-1] == 1:
            # ....11 - 01
            array[i-2] += 1
            del array[i]

        elif array[i] == 1 and array[i-1] != 1:
            # ....11 - 0001
            array[i-1] -= 1
            array.append(1)

        elif array[i] != 1 and array[i-1] == 1:
            # ....11 - 0111
            array[i-2] += 1
            array[i] -= 1

        elif array[i] != 1 and array[i-1] != 1:
            # ....11 - 000111
            array[i] -= 1
            array[i-1] -= 1
            array.insert(i, 1)
            array.insert(i, 1)

    else: # even: 1010
        i = N-2

        if array[i] == 1 and array[i-1] == 1:
            # ....11 - 010
            array[i-2] += 1
            array[i+1] += 1
            del array[i-1]
            del array[i-1]

        elif array[i] == 1 and array[i-1] != 1:
            # ....11 - 0010
            array[i-1] -= 1
            array[i+1] += 1

        elif array[i] != 1 and array[i-1] == 1:
            # ....11 - 0110
            array[i-2] += 1
            array[i-1] += array[i+1]
            array[i] -= 1
            del array[i+1]

        elif array[i] != 1 and array[i-1] != 1:
            # ....11 - 0001110
            # ....11 - 0010011
            array[i-1] -= 1
            array.insert(i, 1)
            array[i+1] -= 1
            array[i+2] += 1
            array[i+1], array[i+2] = array[i+2], array[i+1]

    print len(array)
    print ' '.join(map(str, array))

