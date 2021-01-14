# input 1
# 5
# -15 -6 1 3 7
#
# input 2
# 7
# -15 -4 2 8 9 13 15
#
# input 3
# 7
# -15 -4 3 8 9 13 15

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search(arr, 0, n - 1))