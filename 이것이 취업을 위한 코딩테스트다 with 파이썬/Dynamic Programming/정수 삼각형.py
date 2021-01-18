# input 1
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        target = 0
        if j - 1 >= 0:
            target = max(target, arr[i - 1][j - 1])
        if j < i:
            target = max(target, arr[i - 1][j])
        arr[i][j] += target

print(max(arr[n - 1]))