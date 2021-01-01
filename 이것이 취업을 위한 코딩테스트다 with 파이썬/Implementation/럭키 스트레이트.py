# input
import time
arr = input()

# my sol
start_time = time.time()
length = int(len(arr) / 2)  # f.b: length // 2
head, tail = arr[:length], arr[length:]

sum_head = sum([int(num) for num in head])
sum_tail = sum([int(num) for num in tail])

if sum_head == sum_tail:
    print('LUCKY')
else:
    print('READY')

end_time = time.time()
print('time: ', end_time - start_time)