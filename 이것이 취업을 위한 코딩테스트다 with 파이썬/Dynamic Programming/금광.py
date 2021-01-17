# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

def main(n, m, arr):
    dy = [-1, 0, 1]
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        result[i][0] = arr[i][0]
    for j in range(1, m):
        for i in range(n):
            check = []
            for y in dy:
                if i + y < 0 or i + y >= n:
                    continue
                check.append(result[i + y][j - 1])
            result[i][j] = max(check) + arr[i][j]
    answer = []
    for i in range(n):
        answer.append(result[i][m - 1])
    return max(answer)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr_list = list(map(int, input().split()))
    arr = []
    for idx in range(n):
        arr.append(arr_list[m * idx:m * (idx + 1)])
    print(main(n, m, arr))