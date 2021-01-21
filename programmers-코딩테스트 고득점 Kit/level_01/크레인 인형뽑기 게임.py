# 17 min

def pick(board, pos):
    i = 0
    while i <= len(board) - 1:
        target = board[i][pos - 1]
        if target != 0:
            board[i][pos - 1] = 0
            return board, target
        i += 1
    return board, None

def solution(board, moves):
    answer = 0
    basket = []
    cnt = 0
    for move in moves:
        board, item = pick(board, move)
        if item == None:
            continue
        basket.append(item)
        cnt += 1
        if cnt >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            cnt -= 2
            answer += 2
    return answer