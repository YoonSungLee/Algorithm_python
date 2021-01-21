# 5 min

def solution(numbers):
    results = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            results.append(numbers[i] + numbers[j])
    results = list(set(results))
    results.sort()
    return results  # sorted(list(set(results)))