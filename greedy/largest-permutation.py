if __name__ == '__main__':
    N, K = map(int, raw_input().split())

    array = map(int, raw_input().split())

    S = sorted([[i, array[i]] for i in xrange(N)], key=lambda tuple: tuple[1], reverse=True)
    szip = zip(*S)
    sin = list(szip[0])
    sva = list(szip[1])

    count = 0
    index = 0
    while count < K:
        if index == N: break

        if sin[index] == index:
            index += 1
            continue

        sin[sva.index(array[index])] = sin[index]

        array[sin[index]] = array[index]
        array[index] = sva[index]


        index += 1
        count += 1

    for i in array:
        print i, 
