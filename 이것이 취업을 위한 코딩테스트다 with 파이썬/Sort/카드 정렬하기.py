# # 시간복잡도에서 아슬아슬했던 문제
# # 재풀이 필요
#
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
result = 0
for _ in range(n - 1):
    first = arr.pop()
    second = arr.pop()
    value = first + second
    result += value
    n -= 1
    arr.insert(0, value)
    idx = 0
    for idx in range(n - 1):
        if arr[idx] >= arr[idx + 1]:
            break
        else:
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


print(result)



# sol
# 힙 정렬 이용

import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data =int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)