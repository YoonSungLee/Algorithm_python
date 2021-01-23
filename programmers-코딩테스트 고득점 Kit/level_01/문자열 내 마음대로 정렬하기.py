# 3 min

def solution(strings, n):
    arr = [(string[n], string) for string in strings]
    arr.sort(key=lambda x:(x[0], x[1]))
    return [x[1] for x in arr]

    # sorted(strings, key=lambda x: x[n])