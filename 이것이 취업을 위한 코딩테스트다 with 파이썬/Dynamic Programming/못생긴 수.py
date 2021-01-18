# my sol(풀이와 다름)

n = int(input())

def divide_2(x):
    while True:
        if x % 2 == 0:
            x = x // 2
        else:
            return x

def divide_3(x):
    while True:
        if x % 3 == 0:
            x = x // 3
        else:
            return x

def divide_5(x):
    while True:
        if x % 5 == 0:
            x = x // 5
        else:
            return x

value = 2
cnt = 1
while True:
    k = divide_2(value)
    k = divide_3(k)
    k = divide_5(k)
    if k == 1:
        cnt += 1
    else:
        value += 1
        continue
    if cnt == n:
        print(value)
        break
    else:
        value += 1