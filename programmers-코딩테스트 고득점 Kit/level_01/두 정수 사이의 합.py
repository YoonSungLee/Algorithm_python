# 1 min

def solution(a, b):
    min_val, max_val = min(a, b), max(a, b)
    return sum(range(min_val, max_val + 1))