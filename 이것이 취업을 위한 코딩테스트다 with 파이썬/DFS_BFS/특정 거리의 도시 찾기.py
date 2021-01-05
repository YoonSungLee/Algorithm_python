# 풀이 실패
# input
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
queue = deque()
queue.append(x)

while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if flag == False:
    print(-1)
