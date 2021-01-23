# 2 min

def solution(arr, divisor):
    answer = [element for element in arr if element % divisor == 0]
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer