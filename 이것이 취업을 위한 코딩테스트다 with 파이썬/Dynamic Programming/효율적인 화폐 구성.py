n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

d = [0] * 10001

for money in arr:
    d[money] = 1

def find(x):
    if x < 0:
        return 0
    if d[x] != 0:
        return d[x]
    results = []
    for money in arr:
        result = find(x - money)
        if result != 0:
            results.append(result)
    if len(results) == 0:
        return 0
    d[x] = min(results) + 1
    return d[x]

answer = find(m)
if answer == 0:
    print(-1)
else:
    print(answer)