# input
import time
from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# my sol
start_time = time.time()

answer = 0
check_list = combinations(arr, 2)
for twins in check_list:
    if twins[0] != twins[1]:
        answer += 1

print(answer)

end_time = time.time()
print('time: ', end_time - start_time)

# sol
# 아래 방법은 combinations 함수를 사용하지 않고 문제를 해결한 방법이다.
# 문제 해결에 대한 아이디어가 필요하다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))

array = [0] * 11
for x in arr:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)