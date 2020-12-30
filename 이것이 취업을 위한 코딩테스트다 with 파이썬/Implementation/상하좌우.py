# input
import time
n = int(input())
arr = list(input().split())

# my sol
start_time = time.time()
check_list = [1,2,3,4,5]
pos = [1, 1]
R = [0, 1]
L = [0, -1]
U = [-1, 0]
D = [1, 0]

def direction(step):
    if step == 'R':
        return R
    elif step == 'L':
        return L
    elif step == 'U':
        return U
    else:
        return D

for step in arr:
    direct = direction(step)
    if (pos[0] + direct[0]) in check_list and (pos[1] + direct[1]) in check_list:
        pos[0], pos[1] = pos[0] + direct[0], pos[1] + direct[1]
    else:
        continue
print(pos)

end_time = time.time()
print('time: ', end_time - start_time)

# 시간복잡도: O(N)
# 이러한 이동의 문제는 아래와 같이 dx, dy를 정해놓고 해결하는 것이 깔끔하다.

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)