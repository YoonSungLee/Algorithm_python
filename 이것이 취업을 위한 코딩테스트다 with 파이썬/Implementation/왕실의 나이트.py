# input
import time
data = input()

# my sol
start_time = time.time()
pos = [int(data[1]), ord(data[0]) - 96]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for i in range(len(dx)):
    nx = pos[0] + dy[i]
    ny = pos[1] + dx[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        cnt += 1

print(cnt)

end_time = time.time()
print('time: ', end_time - start_time)