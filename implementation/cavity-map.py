#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(list(grid_t))
    
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):

        if grid[i][j] > grid[i][j+1]:
            if grid[i][j] > grid[i][j-1]:
                if grid[i][j] > grid[i+1][j]:
                    if grid[i][j] > grid[i-1][j]:
                        grid[i][j] = 'X'

                
for g in grid:
    print ''.join(g)
    

