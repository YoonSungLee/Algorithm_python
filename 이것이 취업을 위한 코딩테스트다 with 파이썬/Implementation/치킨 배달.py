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


# book sol
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))    # 일반 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))


    

# my sol
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