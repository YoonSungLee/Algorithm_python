# input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

import time
n, m = map(int, input().split())
y, x, direction = map(int, input().split())
all_map = []
for i in range(n):
    all_map.append(list(map(int, input().split())))

# my sol
start_time = time.time()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
pos = [y, x]
history = []    # 방문 기록

history.append([y, x])  # 처음 위치 --> 방문
turn_time = 0
while True:
    direction = (direction - 1) % 4 # 현재 방향을 기준으로 왼쪽 방향 회전
    nx = pos[1] + dx[direction]
    ny = pos[0] + dy[direction]

    if (all_map[ny][nx] == 0) and ([ny, nx] not in history):     # 방문한 적이 없는 경우
        history.append([ny, nx])
        pos[1], pos[0] = nx, ny
        turn_time = 0
    else:                           # 방문한 적이 있거나 바다인 경우
        turn_time += 1
    if turn_time == 4:              # 네 방향 모두 갈 수 없는 경우
        nx = pos[1] - dx[direction]
        ny = pos[0] - dy[direction]
        if all_map[ny][nx] == 0:    # 뒤로 갈 수 있는 경우
            pos[1], pos[0] = nx, ny
        else:                       # 뒤로 갈 수 없는 경우
            break
        turn_time = 0

print(len(history))
print(history)

end_time = time.time()
print('time: ', end_time - start_time)