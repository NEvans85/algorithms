# https://www.hackerrank.com/challenges/2d-array/problem

import sys

def calc_hourglass(arr, start_pos):
    x, y = start_pos
    total = 0
    total += sum(arr[x][y:y + 3])
    total += arr[x + 1][y + 1]
    total += sum(arr[x + 2][y: y + 3])
    return total

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
    
max_sum = -63
for idx_x in range(4):
    for idx_y in range(4):
        hg_sum = calc_hourglass(arr, [idx_x, idx_y])
        if hg_sum > max_sum:
            max_sum = hg_sum
print (max_sum)

