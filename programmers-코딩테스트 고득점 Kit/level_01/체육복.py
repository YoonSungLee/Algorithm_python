# 21 min

# my sol
def solution(n, lost, reserve):
    # 여분이 있지만 도난당한 사람은 두 경우에 대하여 제외
    intersect = set(lost) & set(reserve)
    lost = list(set(lost) - set(intersect))
    reserve = list(set(reserve) - set(intersect))

    # 체육복 소지 학생 초기화
    students = [1] * (n + 1)
    students[0] = 0
    for p in lost:
        students[p] = 0

    for p in reserve:
        if p - 1 in lost:   # 앞사람이 체육복이 없는 경우
            lost.remove(p - 1)
            students[p - 1] = 1
        elif p + 1 in lost: # 뒷사람이 체육복이 없는 경우
            lost.remove(p + 1)
            students[p + 1] = 1

    return sum(students)



# other sol
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)