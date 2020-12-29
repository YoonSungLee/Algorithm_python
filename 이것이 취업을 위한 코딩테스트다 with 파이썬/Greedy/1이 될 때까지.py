# input
import time
n, k = map(int, input().split())
cnt = 0

# my sol
start_time = time.time()
while True:
    if n == 1:
        break
    elif n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

end_time = time.time()
print('time :', end_time - start_time)

# sol
# k로 나눌 수 있는 값이 될 때까지의 과정을 한 번에 수행하는 방법이다.
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += n - target
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)