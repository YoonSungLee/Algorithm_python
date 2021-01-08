# 단순히 순열로 풀었지만, 좀 더 시간복잡도를 줄이기 위해서는 '중복 순열' 방법을 이용해야 한다.
# 또한 교재에서는 이를 'DFS&BFS' 파트로 분류했으므로, 구현이 아닌 DFS&BFS 파트에 대한 풀이도 할 수 있어야 한다.

# input 1
# 2
# 5 6
# 0 0 1 0

# input 2
# 3
# 3 4 5
# 1 0 1 0

# input 3
# 6
# 1 2 3 4 5 6
# 2 1 1 1

# my sol
# implementation

from itertools import permutations

def calculation(a, b, cal):
    if cal == 0:
        return a + b
    elif cal == 1:
        return a - b
    elif cal == 2:
        return a * b
    else:
        if a >= 0:
            return a // b
        else:
            return - (- a // b)

n = int(input())
numbers = list(map(int, input().split()))
cal_list = []
for cal, number in enumerate(map(int, input().split())):
    cal_list += [cal for _ in range(number)]

results = []
for cals in permutations(cal_list, len(cal_list)):
    result = numbers[0]
    for cal, number in zip(cals, numbers[1:]):
        result = calculation(result, number, cal)
    results.append(result)

print(max(results))
print(min(results))



# sol
# DFS
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))  # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)