def solution(n, lost, reserve):
    students = [1] * (n + 1)
    students[0] = 0
    for p in lost:
        students[p] = 0

    for p in reserve:
        if p in lost:
            lost.remove(p)
        elif p - 1 in lost:
            lost.remove(p - 1)
            students[p - 1] = 1
        elif p + 1 in lost:
            lost.remove(p + 1)
            students[p + 1] = 1
    return sum(students)

print(solution(3, [1, 2], [2, 3]))