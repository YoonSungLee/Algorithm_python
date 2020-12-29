# input
import time
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

# my sol
start_time = time.time()

numbers.sort()
numbers = numbers[::-1] # f.b: 굳이 뒤집을 필요는 없다고 판단

first, second = numbers[0], numbers[1]
count = (m // (k + 1)) * k + (m % (k + 1))

answer = first * count + second * (m - count)
end_time = time.time()
print(answer)

end_time = time.time()
print('time :', end_time - start_time)