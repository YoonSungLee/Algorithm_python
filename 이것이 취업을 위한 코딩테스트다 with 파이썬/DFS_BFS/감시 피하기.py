# input 1
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# input 2
# 4
# S S S T
# X X X X
# X X X X
# T T T X


# 감시를 피할 수 있는지 확인
def check_map(current_map):
    global n
    for i in range(n):
        for j in range(n):
            if current_map[i][j] == 'T':    # T의 좌표들을 미리 저장해두어 그 부분만 곧바로 탐색할 수도 있다.
                if dfs_up(i - 1, j, current_map) or dfs_down(i + 1, j, current_map)\
                    or dfs_left(i, j - 1, current_map) or dfs_right(i, j + 1, current_map):
                    return False
    return True

# 학생을 잡을 수 있는지 확인
def dfs_up(i, j, current_map):
    if i < 0:
        return False
    else:
        if current_map[i][j] == 'S':
            return True
        elif current_map[i][j] == 'O':
            return False
        else:
            return False or dfs_up(i - 1, j, current_map)

def dfs_down(i, j, current_map):
    global n
    if i >= n:
        return False
    else:
        if current_map[i][j] == 'S':
            return True
        elif current_map[i][j] == 'O':
            return False
        else:
            return False or dfs_down(i + 1, j, current_map)

def dfs_left(i, j, current_map):
    if j < 0:
        return False
    else:
        if current_map[i][j] == 'S':
            return True
        elif current_map[i][j] == 'O':
            return False
        else:
            return False or dfs_left(i, j - 1, current_map)

def dfs_right(i, j, current_map):
    global n
    if j >= n:
        return False
    else:
        if current_map[i][j] == 'S':
            return True
        elif current_map[i][j] == 'O':
            return False
        else:
            return False or dfs_right(i, j + 1, current_map)

from itertools import combinations

n = int(input())
all_map = []
for _ in range(n):
    all_map.append(list(input().split()))

obstacles_list = []
for i in range(n):
    for j in range(n):
        if all_map[i][j] == 'X':
            obstacles_list.append([i, j])

result = 'NO'
for obstacles in combinations(obstacles_list, 3):
    for x, y in obstacles:
        all_map[x][y] = 'O'
    if check_map(all_map):
        result = 'YES'
        break
    for x, y in obstacles:
        all_map[x][y] = 'X'

print(result)