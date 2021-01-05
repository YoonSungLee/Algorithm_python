# input 1
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# input 2
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# input 3
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0

from itertools import combinations
import copy

n, m = map(int, input().split())

# map setting
all_map = []
for _ in range(n):
    all_map.append(list(map(int, input().split())))

zero_list = []
for row in range(n):
    for col in range(m):
        if all_map[row][col] == 0:
            zero_list.append([row, col])

combi_list = list(combinations(zero_list, 3))

results = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j):
    tmp_map[i][j] = 2
    for k in range(4):
        n_i, n_j = i + dx[k], j + dy[k]
        if n_i < 0 or n_j < 0 or n_i > n - 1 or n_j > m - 1:
            continue
        if tmp_map[n_i][n_j] == 0:
            dfs(n_i, n_j)


# 각 경우에 대하여 시뮬레이션 수행
for combi in combi_list:
    tmp_map = copy.deepcopy(all_map)

    # 벽 3개 세우기
    for row, col in combi:
        tmp_map[row][col] = 1

    # 바이러스 전파
    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 2:
                dfs(i, j)

    # 0의 개수 카운트
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 0:
                cnt += 1

    results.append(cnt)

print(max(results))