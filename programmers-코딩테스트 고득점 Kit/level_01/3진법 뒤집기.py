# 7 min

# my sol
def solution(n):
    number_3 = ''
    while True:
        if n < 3:
            number_3 = str(n) + number_3
            break
        number_3 = str(n % 3) + number_3
        n = n // 3

    answer = 0
    for idx, num in enumerate(number_3):
        answer += int(num) * (3 ** int(idx))
    return answer