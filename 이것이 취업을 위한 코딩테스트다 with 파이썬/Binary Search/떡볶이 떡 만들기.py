# input
# 4 6
# 19 15 10 17

n, m = map(int, input().split())
arr = list(map(int, input().split()))

end = max(arr)
start = min(arr)
result = []

def calculation(length, arr):
    return sum([max(0, x - length) for x in arr])

def binary_search(start, end, arr):
    if start > end:
        return
    mid = (start + end) // 2
    get_length = calculation(mid, arr)
    if get_length == m:
        result.append(mid)
        binary_search(mid + 1, end, arr)
    elif get_length > m:
        binary_search(mid + 1, end, arr)
    else:
        binary_search(start, mid - 1, arr)

binary_search(start, end, arr)
print(max(result))