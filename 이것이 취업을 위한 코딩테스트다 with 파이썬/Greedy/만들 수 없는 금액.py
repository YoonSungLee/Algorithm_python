# input
import time
from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# my sol
def check_function(num, arr):
    for i in range(1, n+1):
        check_list = []
        combination_list = combinations(arr, i)
        for num_list in combination_list:
            check_list.append(sum(num_list))
        if num in check_list:
            return True
    return False

for i in range(1, max(arr)+1):
    if check_function(i, arr):
        continue
    else:
        print(i)
        break

# sol
# 문제 해결 방법에 대한 아이디어가 있으면 아래처럼 굉장히 단순하게 코드를 작성할 수 있다.
# 이는 문제 해결 아이디어를 충분히 고려해야 할 필요성을 보여준다.
# 현재 상태를 '1부터 target - 1까지의 모든 금액을 만들 수 있는 상태'라고 보자.
# 이때 매번 target인 금액도 만들 수 있는지(현재 확인하는 동전의 단위가 target 이하인지) 체크하는 아이디어이다.

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    else:
        target += x

print(target)