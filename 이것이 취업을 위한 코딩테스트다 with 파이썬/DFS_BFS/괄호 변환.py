# check function 구현 시 stack list를 사용하지 않고도 구현 가능
# def check_function(p):
#     count = 0   # 왼쪽 괄호의 개수
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
#                 return False
#             count -= 1
#     return True # 쌍이 맞는 경우에 True 반환

def solution(target):
    if target == "":
        return ""
    u, v = split_function(target)
    if check(u):
        result = u + solution(v)
    else:
        result = "(" + solution(v) + ")" + reverse(u[1 : len(u) - 1])   # u[1:-1]: 첫 번째와 마지막 문자를 제거
    return result

def split_function(target):
    u = ""
    for pos in target:
        u += pos
        count = 0
        for i in u:
            if i == "(":
                count += 1
            else:
                count -= 1
        if count == 0:
            break
    return u, target[len(u):]

def check(target):
    stack = []
    for i in target:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def reverse(target):
    result = ""
    for i in target:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result

# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))