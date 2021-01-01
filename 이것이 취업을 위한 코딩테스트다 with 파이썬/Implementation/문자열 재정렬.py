# input
import time
arr = input()
alpha, number = '', 0

for pos in arr:
    if pos.isdigit():
        number += int(pos)
    else:
        alpha += pos

print(''.join(sorted(alpha)) + str(number))

end_time = time.time()
print('time: ', end_time - start_time)