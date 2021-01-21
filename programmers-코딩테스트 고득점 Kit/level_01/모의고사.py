# 20 min

# my sol
def solution(answers):
    result = [[1, 0], [2, 0], [3, 0]]   # result = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        if answer == one[idx % 5]:
            result[0][1] += 1
        if answer == two[idx % 8]:
            result[1][1] += 1
        if answer == three[idx % 10]:
            result[2][1] += 1

    max_val = max(result[0][1], result[1][1], result[2][1]) # max_val = max(result)
    answer = [i[0] for i in result if i[1] == max_val]
    answer.sort()
    return answer

    # answer = []
    # for idx, val in enumerate(result):
    #     if val == max_val:
    #         answer.append(idx + 1)
    #
    # return answer