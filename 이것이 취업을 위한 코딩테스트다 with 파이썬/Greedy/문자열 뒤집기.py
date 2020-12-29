# input
import time
numbers = input()

# my sol
start_time = time.time()

zero_cnt = 0
one_cnt = 0
before_num = numbers[0]

for i in range(1, len(numbers)):
    if before_num == numbers[i]:
        continue
    else:
        if before_num == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
        before_num = numbers[i]

print(min(zero_cnt, one_cnt))

end_time = time.time()
print('time :', end_time - start_time)