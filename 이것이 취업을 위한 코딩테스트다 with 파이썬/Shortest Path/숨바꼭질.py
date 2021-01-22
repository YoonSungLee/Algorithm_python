# input 1
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
INF = float('inf')
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dijkstra(1)
safest = max(distance[2:])
positions = []
for node, dis in enumerate(distance):
    if dis == safest:
        positions.append(node)
print(min(positions), safest, len(positions))