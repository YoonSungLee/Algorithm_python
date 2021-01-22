import heapq

n, m, c = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

INF = float('inf')
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
times = []
for i in range(1, n + 1):
    if i == c:
        continue
    if distance[i] != INF:
        cnt += 1
        times.append(distance[i])

print(cnt, max(times))