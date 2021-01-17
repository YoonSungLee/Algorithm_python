# my sol(테스트 케이스가 적어서 판별하기 어려움)
# sol과 다른 방법

n = int(input())
arr = list(map(int, input().split()))
result = [0] * n
result[0], result[1], result[2] = arr[:3]

for idx, item in enumerate(arr):
    if idx == 0 or idx == 1 or idx == 2:
        continue
    result[idx] = max(arr[idx - 2], arr[idx - 3]) + item

print(max(result))



# sol
# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])