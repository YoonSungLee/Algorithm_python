# 정답은 맞췄지만 시간이 오래 걸리고 효율적이지 못한 코드 작성이 문제점
# (1, 1)부터 시작하고 0의 index를 갖는 데이터들의 활용도가 없을 때(예: 벽으로 막혀져 있다)
# (0, 0)부터 제어하는 것보단 다음과 같은 방법이 직관적일 수 있다.
# 가로 및 세로 크기를 1씩 늘린 list를 생성 후 (1, 1)부터 제어하는 방식을 사용한다.

# input 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# input 2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# input 3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L


# my sol
from collections import deque
import sys

n = int(input())
k = int(input())

road_map = [[0] * n for _ in range(n)]

# apple setting
for _ in range(k):
    row, col = map(int, input().split())
    road_map[row-1][col-1] = 'apple'

# moving info setting
l = int(input())
info = []
index = 0
for _ in range(l):
    x, c = input().split()
    info.append([int(x), c])
info.append([float('inf'), 'D'])

queue = deque()
queue.append([0, 0])

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = 1
seconds = 0

# game start
while True:
    pos_y, pos_x = queue[-1]    # 현재 머리의 위치
    n_x, n_y = (pos_x + dx[direction]), (pos_y + dy[direction])
    if n_x < 0 or n_x > n - 1 or n_y < 0 or n_y > n - 1 or [n_y, n_x] in queue:
        seconds += 1
        break
    else:
        queue.append([n_y, n_x])
        seconds += 1
        if road_map[n_y][n_x] == 'apple':
            road_map[n_y][n_x] = 0
        else:
            queue.popleft()
    if seconds == info[index][0]:
        if info[index][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        index += 1
print(seconds)


# book sol
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in rnage(n+1)]    # 맵 정보
info = []   # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1     # 뱀의 머리 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0   # 처음에는 동쪽을 보고 있음
    time = 0        # 시작한 뒤에 지난 '초' 시간
    index = 0       # 다음에 회전할 정보
    q = [(x,y)]     # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
            data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny   # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]:    # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())