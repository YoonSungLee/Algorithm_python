# input 1
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# input 2
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# input 3
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# input 4
# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1

from itertools import combinations
import copy

def cal_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def cal_city_distance(house_list, chicken_list):
    city_distance = 0
    for house in house_list:
        chicken_distance = 999
        for chicken in chicken_list:
            distance = cal_distance(house, chicken)
            chicken_distance = min(distance, chicken_distance)
        city_distance += chicken_distance
    return city_distance

n, m = map(int, input().split())
all_map = []
for _ in range(n):
    all_map.append(list(map(int, input().split())))

house_list = []
chicken_list = []

for i in range(n):
    for j in range(n):
        target = all_map[i][j]
        if target == 1:
            house_list.append([i, j])
        elif target == 2:
            chicken_list.append([i, j])

choice_list = combinations(chicken_list, m) # m개의 치킨집을 고르는 모든 경우의 수(최대?)

results = []
for removed_chicken_list in choice_list:
    city_distance = cal_city_distance(house_list, removed_chicken_list) # 도시의 치킨 거리 계산
    results.append(city_distance)

print(min(results))