# input 1
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# input 2
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2

# 시간 제한으로 풀이 실패
# 실질적으로 bfs를 사용하지 않은 코드
##################################################
import copy

n, k = map(int, input().split())
all_map = []
for _ in range(n):
    all_map.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move_virus(virus):
    for i in range(n):
        for j in range(n):
            if before_map[i][j] == virus:
                for idx in range(4):
                    x = i + dx[idx]
                    y = j + dy[idx]
                    if x >= 0 and y >= 0 and x < n and y < n and before_map[x][y] == 0:
                        after_map[x][y] = virus


before_map = copy.deepcopy(all_map)
after_map = copy.deepcopy(all_map)

for _ in range(s):
    for virus in range(1, k+1):
        move_virus(virus)
        before_map = copy.deepcopy(after_map)

print(after_map[x-1][y-1])
##################################################


from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []   # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])