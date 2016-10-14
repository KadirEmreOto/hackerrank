

def NonContiguous(array):
    m = max(array)
    if m <= 0:
        return m
    c = 0
    for i in array:
        if i > 0 :
            c += i
    return c

def Shrink(array):
    temp = []
    mid = array[0]

    result = max(array)
    
    if result <= 0:
        return [result]

    for i in xrange(array.count(0)):
        array.remove(0)

    for index in xrange(1, len(array)):
        if array[index] * array[index-1] < 0 :
            temp.append(mid)
            mid = array[index]
        else:
            mid += array[index]
    temp.append(mid)

    return temp


def Contiguous(array):
    i = 0
    for item in array:
        if item < 0:
            i += 1
        else:
            break

    if i == len(array): return max(array)

    sum_ = array[i]
    result = sum_
    for k in array[i+1:]:
        sum_ += k
        if  sum_ < 0:
            sum_ = 0

        else:
            if sum_ > result:
                result = sum_


    return result

T = raw_input().strip()

for _ in xrange(int(T)):
    size = raw_input()
    array = map(int, raw_input().split())

    print Contiguous(Shrink(array)), NonContiguous(array)




