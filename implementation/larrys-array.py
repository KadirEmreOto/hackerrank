

T = int(raw_input())
for _ in xrange(T):
    try:
        N = int(raw_input())
        array = map(int, raw_input().split())
        array = [[array[i], i] for i in xrange(N)]

        ordered = sorted(array)

        for i in xrange(N):
            number, index = ordered[i]

            if (index - i) % 2: # ODD
                for k in xrange(i, index):
                    array[k], array[index] = array[index], array[k]
                    array[k][1] = k
                    array[index][1] = index

                array[i+1], array[i+2] = array[i+2], array[i+1]
                array[i+1][1] = i+1
                array[i+2][1] = i+2

            else: # EVEN
                for k in xrange(i, index):
                    array[k], array[index] = array[index], array[k]
                    array[k][1] = k
                    array[index][1] = index

        print 'YES'
    except:
        print 'NO'
