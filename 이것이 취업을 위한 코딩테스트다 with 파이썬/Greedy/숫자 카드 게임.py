# input
import time
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# my sol
start_time = time.time()

max_list = []
for row in arr:
    max_list.append(min(row))

print(max(max_list))

end_time = time.time()
print('time :', end_time - start_time)

# sol
# 저자의 sol은 input과 동시에 문제를 해결하는 방식이다.
# 해당 방법이 my sol보다 simple함을 알 수 있다.
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)