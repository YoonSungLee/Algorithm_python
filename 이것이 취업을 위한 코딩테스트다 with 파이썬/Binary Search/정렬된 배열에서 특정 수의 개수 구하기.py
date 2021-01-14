# input 1
# 7 2
# 1 1 2 2 2 2 3
#
# input 2
# 7 4
# 1 1 2 2 2 2 3

# 시간 초과 가능성이 높은 코드
# sol을 참고할 것: 1) 직접 구현 2) 라이브러리 사용
import sys

n, x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

idx = binary_search(arr, x, 0, n - 1)
if idx == -1:
    print(-1)
else:
    left_idx = idx
    right_idx = idx
    while True:
        if arr[left_idx] != x or left_idx < 0:
            break
        left_idx -= 1
    while True:
        if arr[right_idx] != x or right_idx >= n:
            break
        right_idx += 1
    print(right_idx - left_idx - 1)