# input 1
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1

for i in range(1 + n):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for a in range(1 + n):
    cnt = 0
    for b in range(1 + n):
        if graph[a][b] != 0 and graph[a][b] != INF:
            cnt += 1
        if graph[b][a] != 0 and graph[b][a] != INF:
            cnt += 1
    if cnt == n - 1:
        answer += 1

print(answer)