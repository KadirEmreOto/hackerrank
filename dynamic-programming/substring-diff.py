import heapq
from collections import defaultdict

def community(word1, word2):
    length = len(word1)
    matrix = [[0]*length for i in xrange(length)]

    for i in xrange(length):
        for j in xrange(length):
            if word1[i] == word2[j]:
                matrix[i][j] = 1
    return matrix

def flatten(matrix, i, j):
    c = 1
    array = [0]
    last  = matrix[i][j]
    length = len(matrix)

    if last == 0: array[0] += 1
    else: array.append(1)

    while i + c != length and j + c != length:
        if matrix[i + c][j + c] == last:
            array[-1] += 1
        else:
            last = matrix[i + c][j + c]
            array.append(1)
        c += 1
    return array

def construct(matrix):
    length = len(matrix)
    arrays = [flatten(matrix, 0, 0)]

    for i in xrange(1, length):
        arrays.append(flatten(matrix, 0, i))
        arrays.append(flatten(matrix, i, 0))
    return arrays

def solve(array, i, k):
    #print '#', i, k
    if i in dp and k in dp[i]: return dp[i][k]

    if i == len(array): return 0

    if i & 1:
        answer = array[i] + solve(array, i + 1, k)

    elif k < array[i]:
        answer = k

    else:
        answer = array[i] + solve(array, i + 1, k - array[i])

    if i not in dp: dp[i] = {}
    dp[i][k] = answer
    return answer



for t in xrange(input()):
    line = raw_input().split()

    length = int(line[0])
    word1 = line[1]
    word2 = line[2]

    c = community(word1, word2)

    answer = 0
    arrays = construct(c)
    """
    for i in c:
        for j in i:
            print j,
        print
    """
    for array in arrays:
        dp = {}
        for i in xrange(len(array)):
            #print i, array, solve(array, i, length)
            answer = max(solve(array, i, length), answer)

    print answer

