# 3 min

# my sol
def solution(array, commands):
    answer = []
    for start, end, order in commands:
        target = array[start - 1: end]
        target.sort()
        answer.append(target[order - 1])
    return answer