# input
import time
n = int(input())
arr = list(map(int, input().split()))
cnt = 0

# my sol
start_time = time.time()
arr.sort()
while len(arr) != 0:
    group = arr[:arr[0]]
    if max(group) == arr[0]:
        cnt += 1
        arr = arr[arr[0]:]
    else:
        if len(arr) < max(group):
            break
        else:
            cnt += 1
            arr = arr[max(group):]

print(cnt)

end_time = time.time()
print('time : %.7f'%(end_time - start_time))


# sol
# array를 조절하지 않고 단순히 순회를 하면서 문제의 조건을 파악하며 해결해나간다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)