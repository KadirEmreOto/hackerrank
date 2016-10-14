#-*- coding: utf-8 -*-
from collections import defaultdict

mod = 10**9+7
moves = (
    ((0, 1), (0, 2), (1, 2)),   # r r d
    ((1, 0), (1, 1), (1, 2)),   # d r r
    ((0, 1), (1, 1), (2, 1)),   # r d d
    ((1, 0), (2, 0), (2, 1)),   # d d r
    ((0, 1), (0, 2), (1, 0)),   # r r d [Q]
    ((0, 1), (1, 0), (2, 0)),   # r d d [Q]
    ((1, 0), (1,-1), (1,-2)),   # d l l
    ((1, 0), (2, 0), (2,-1))    # d d l
)


def Solve(i, j):
    if i >= N-1: return 0
    if j < M and not grid[i] & (1 << (M-j-1)): return Solve(i, j+1)

    cache = tuple(grid)
    if not any(cache): return 1
    if cache in dp[M]: return dp[M][cache]

    if j >= M: return Solve(i+1, 0)

    grid[i] -= (1<<(M-1-j))
    answer = 0
    for points in moves:
        check = True
        for x, y in points:
            if (not (0 <= x+i < N and 0 <= y+j < M)) or not grid[x+i] & (1 << M-y-j-1):
                check = False
                break

        if check:
            for x, y in points: grid[x+i] -= (1 << (M-y-j-1))
            answer += Solve(i, j+1)
            answer %= mod
            for x, y in points: grid[x+i] += (1 << (M-y-j-1))

    grid[i] += (1 << (M-1-j))
    answer %= mod
    dp[M][cache] = answer
    return answer

dp = defaultdict(dict)
T = int(raw_input())
for t in xrange(1, T+1):
    N, M = map(int, raw_input().split())
    grid = [0] * N
    empty = 0

    for i in xrange(N):
        line = raw_input()
        for j in xrange(M-1, -1, -1):
            if line[j] == '.':
                grid[i] += 1 << (M-j-1)
                empty += 1

    if not empty: print 1
    elif empty % 4: print 0
    else: print Solve(0, 0)

