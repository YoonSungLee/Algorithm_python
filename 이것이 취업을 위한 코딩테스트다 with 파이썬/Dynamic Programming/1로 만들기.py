def make_one(x):
    if x == 1:
        return None
    elif arr[x] != 0:
        return arr[x]
    else:
        answer = []
        if x % 5 == 0:
            answer.append(make_one(x // 5))
        if x % 3 == 0:
            answer.append(make_one(x // 3))
        if x % 2 == 0:
            answer.append(make_one(x // 2))
        answer.append(make_one(x - 1))
        arr[x] = min(answer) + 1
        return arr[x]

x = int(input())

arr = [0 for _ in range(30001)]     # [0] * 30001
arr[2], arr[3], arr[5] = 1, 1, 1

print(make_one(x))