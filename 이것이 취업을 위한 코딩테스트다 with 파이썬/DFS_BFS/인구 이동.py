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

from collections import deque
import copy

n, l, r = map(int, input().split())
all_map = []
for _ in range(n):
    all_map.append(list(map(int, input().split())))

count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    after_map = copy.deepcopy(all_map)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                queue = deque()
                population = all_map[i][j]
                queue.append([i, j, all_map[i][j]])
                union_city_list = [[i, j]]
                while queue:
                    x, y, before_pop = queue.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if nx < 0 or nx >= n or ny < 0 or ny >=n:
                            continue
                        if visited[nx][ny] == True:
                            continue
                        current_pop = all_map[nx][ny]
                        if l <= abs(before_pop - current_pop) <= r:
                            population += current_pop
                            union_city_list.append([nx, ny])
                            queue.append([nx, ny, current_pop])
                            visited[nx][ny] = True
                mean_pop = int(population / len(union_city_list))
                for x, y in union_city_list:
                    after_map[x][y] = mean_pop
    if after_map == all_map:
        break
    else:
        count += 1
        all_map = after_map

print(count)