# input
import sys
import time
arr = input()

# my sol
start_time = time.time()
answer = int(arr[0])
check_list = [0, 1]

if len(arr) == 1:   # 하나의 입력값만을 받는 경우
    print(answer)
    sys.exit()

for num in arr[1:]:
    num = int(num)
    if answer in check_list or num in check_list:   # f.b : answer <= 1 or num <= 1
        answer += num
    else:
        answer *= num

print(answer)

end_time = time.time()
print('time :', end_time - start_time)