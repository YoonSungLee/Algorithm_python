# 6 min

# my sol
def solution(arr):
    answer = []
    last = 'tmp'    # arr[-1:]
    for num in arr:
        if num != last:
            answer.append(num)
            last = num
    return answer