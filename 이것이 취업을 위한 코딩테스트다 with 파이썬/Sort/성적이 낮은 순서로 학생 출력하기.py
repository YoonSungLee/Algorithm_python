# point
# 학생의 정보가 최대 100,000개까지 입력될 수 있으므로
# 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나
# O(N)을 보장하는 계수 정렬을 이용하면 된다.

n = int(input())
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append([name, score])

arr.sort(key=lambda x:x[1])

for i in range(n):
    print(arr[i][0], end=' ')