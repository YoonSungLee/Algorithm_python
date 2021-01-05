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