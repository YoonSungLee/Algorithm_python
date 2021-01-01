# input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
import time
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# my sol
# 최단 경로 문제 아이디어: BFS + ((다음 노드의 값) = (이전 노드의 값) + 1)
from collections import deque
start_time = time.time()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    if (x == n - 1) and (y == m - 1):
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])

end_time = time.time()
print('time :', end_time - start_time)