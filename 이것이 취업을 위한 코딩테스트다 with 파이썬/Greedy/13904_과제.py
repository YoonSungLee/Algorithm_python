# 7
# 4 60
# 4 40
# 1 20
# 2 50
# 3 30
# 4 10
# 6 5

N = int(input())
homeworks = []
for _ in range(N):
    homeworks.append(list(map(int, input().split())))
homeworks.sort(key=lambda x: x[1], reverse=True)

days = [False] * 1001
answer = 0

for day, score in homeworks:
    # 과제 해결할 수 있는 day 중에 가장 먼 쪽을 채택하기
    while day != 0:
        if days[day] == False:
            answer += score
            days[day] = True
            break   # break를 하지 않으면 채택 이후 계속 while문 순환
        else:
            day -= 1

print(answer)