# Recursion Error
# input 1
# 2 20 50
# 50 30
# 20 40

# input 2
# 2 40 50
# 50 30
# 20 40

# input 3
# 2 20 50
# 50 30
# 30 40

# input 4
# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# input 5
# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10

import copy

def dfs(x, y, before_pop):
    global n, l, r, populations
    if x < 0 or x >= n or y < 0 or y >= n:
        return None
    if visited[x][y] == True:
        return None
    current_pop = all_map[x][y]
    diff = abs(before_pop - current_pop)
    if diff < l or diff > r:
        return None
    visited[x][y] = True
    union_city_list.append([x, y])
    populations += current_pop
    dfs(x - 1, y, current_pop)
    dfs(x + 1, y, current_pop)
    dfs(x, y - 1, current_pop)
    dfs(x, y + 1, current_pop)


n, l, r = map(int, input().split())
all_map = []
for _ in range(n):
    all_map.append(list(map(int, input().split())))

cnt = 0
while True:
    after_map = copy.deepcopy(all_map)
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            else:
                visited[i][j] = True
                union_city_list = [[i, j]]
                pop = all_map[i][j]
                populations = pop
                dfs(i - 1, j, pop)
                dfs(i + 1, j, pop)
                dfs(i, j - 1, pop)
                dfs(i, j + 1, pop)
                mean_pop = int(populations / len(union_city_list))
                for x, y in union_city_list:
                    after_map[x][y] = mean_pop
    # 인구 이동을 마친 후
    if after_map == all_map:    # 변화가 없으면
        break
    else:                       # 변화가 있으면
        cnt += 1
        all_map = after_map

print(cnt)
