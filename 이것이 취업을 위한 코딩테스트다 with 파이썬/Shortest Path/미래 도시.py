# input 1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# input 2
# 4 2
# 1 3
# 2 4
# 3 4

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1
x, k = map(int, input().split())
for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][k] + graph[k][x]
if answer == INF:
    print(-1)
else:
    print(answer)