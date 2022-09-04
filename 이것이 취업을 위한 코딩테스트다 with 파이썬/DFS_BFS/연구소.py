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

# from itertools import combinations
# import copy
#
# n, m = map(int, input().split())
#
# # map setting
# all_map = []
# for _ in range(n):
#     all_map.append(list(map(int, input().split())))
#
# zero_list = []
# for row in range(n):
#     for col in range(m):
#         if all_map[row][col] == 0:
#             zero_list.append([row, col])
#
# combi_list = list(combinations(zero_list, 3))
#
# results = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def dfs(i, j):
#     tmp_map[i][j] = 2
#     for k in range(4):
#         n_i, n_j = i + dx[k], j + dy[k]
#         if n_i < 0 or n_j < 0 or n_i > n - 1 or n_j > m - 1:
#             continue
#         if tmp_map[n_i][n_j] == 0:
#             dfs(n_i, n_j)
#
#
# # 각 경우에 대하여 시뮬레이션 수행
# for combi in combi_list:
#     tmp_map = copy.deepcopy(all_map)
#
#     # 벽 3개 세우기
#     for row, col in combi:
#         tmp_map[row][col] = 1
#
#     # 바이러스 전파
#     for i in range(n):
#         for j in range(m):
#             if tmp_map[i][j] == 2:
#                 dfs(i, j)
#
#     # 0의 개수 카운트
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if tmp_map[i][j] == 0:
#                 cnt += 1
#
#     results.append(cnt)
#
# print(max(results))



# book sol
n, m = map(int, input().split())
data = []   # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                # temp: 벽 설치 이후 바이러스가 퍼진 이후 결과 map
                # data: 벽 설치까지만
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)