#-*- coding: utf-8 -*-
# 1 2 3 4 4 5 6 7 8 
# 4 4 4 5 4 3 2 1 0

# 1 1 1 1 1 1 3 4 5 20
# 8 7 6 5 4 3 3 2 0 0

if __name__ == '__main__':
    N = int(raw_input())
    array = map(int, raw_input().split())
    array = sorted(array)

    dn = [1]
    i = 0
    j = 1
    while i < N:
        w1 = array[i]

        count = 0
        while True:
            if i + j > N-1:
                break

            w2 = array[i+j]
            if w2 - w1 < 5 :
                j += 1
                count += 1
            else:
                break
        dn.append(dn[-1] - 1 + count)

        i += 1
        j -= 1

    dn = dn[1:]
# 1 4 4 5 4 3 2 1 0             6 5 4 3 2 1 0 
    answer = 0
    i = N-1
    while i > -1:
        if dn[i] < dn[i-1]:
            i -= 1
            continue
        else:
            if i == 0:
                answer += 1
                break

            j = 0
            while True:
                j += 1
                if dn[i-j] > j - 1:
                    dn[i-j] = j - 1
                else:
                    break

            if j == 1:
                i -= 1
            else:
                i -= j-1

            answer += 1

    print answer
