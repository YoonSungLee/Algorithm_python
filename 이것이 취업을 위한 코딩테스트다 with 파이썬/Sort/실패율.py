def solution(N, stages):
    count = [0] * (N + 2)
    for stage in stages:
        count[stage] += 1

    answer = []
    total = len(stages)

    for i in range(1, N + 1):
        if total == 0:
            answer.append([i, 0])
            continue
        answer.append([i, count[i] / total])
        total -= count[i]

    answer.sort(key= lambda x:(-x[1], x[0]))

    result = []
    for stage, percent in answer:
        result.append(stage)
    return result