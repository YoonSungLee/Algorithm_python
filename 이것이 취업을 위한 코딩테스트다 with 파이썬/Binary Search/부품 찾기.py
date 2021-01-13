# sol을 통해 다양한 접근 방법 살펴보기
# input
# 5
# 8 3 7 9 2
# 3
# 5 7 9

n = int(input())
item_list = list(map(int, input().split()))
item_list.sort()
m = int(input())
want_list = list(map(int, input().split()))

result = []

for target in want_list:
    start = 0
    end = n - 1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if item_list[mid] == target:
            result.append('yes')
            flag = True
            break
        elif item_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if flag:
        continue
    result.append('no')

for answer in result:
    print(answer, end=' ')