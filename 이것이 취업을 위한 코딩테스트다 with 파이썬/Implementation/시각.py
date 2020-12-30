# input
import time
hours = int(input()) + 1

# my sol
start_time = time.time()
cnt = 0

for hour in range(hours):
    for minute in range(60):
        for second in range(60):
            if '3' in (str(hour) + str(minute) + str(second)):
                cnt += 1

print(cnt)

end_time = time.time()
print('time: ', end_time - start_time)


# 모든 시각의 경우를 하나씩 모두 세서 쉽게 풀 수 있는 문제 --> 완전 탐색 유형
# 모든 경우의 수가 86,400가지이기 때문
# 따라서 100,000개도 되지 않으므로 파이썬에서 문자열 연산을 이용해 3이 시각에 포함되어 있는지 확인해도 시간 제한 2초 안에 문제를 해결할 수 있다.