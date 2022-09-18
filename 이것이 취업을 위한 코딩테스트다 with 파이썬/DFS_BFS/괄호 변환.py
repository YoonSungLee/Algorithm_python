### 기본 코드
# def solution(p):
#     answer = ''
#     return answer


# book solution
def balanced_index(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count +=1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    # 빈 문자인 경우 빈 문자 반환
    if p == '':
        return answer

    # 균형 잡힌 괄호의 최소 단위 u 찾기
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    # "올바른 괄호 문자열" 이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])   # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer



# my solution
# # check function 구현 시 stack list를 사용하지 않고도 구현 가능
# # def check_function(p):
# #     count = 0   # 왼쪽 괄호의 개수
# #     for i in p:
# #         if i == '(':
# #             count += 1
# #         else:
# #             if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
# #                 return False
# #             count -= 1
# #     return True # 쌍이 맞는 경우에 True 반환
#
# def solution(target):
#     if target == "":
#         return ""
#     u, v = split_function(target)
#     if check(u):
#         result = u + solution(v)
#     else:
#         result = "(" + solution(v) + ")" + reverse(u[1 : len(u) - 1])   # u[1:-1]: 첫 번째와 마지막 문자를 제거
#     return result
#
# def split_function(target):
#     u = ""
#     for pos in target:
#         u += pos
#         count = 0
#         for i in u:
#             if i == "(":
#                 count += 1
#             else:
#                 count -= 1
#         if count == 0:
#             break
#     return u, target[len(u):]
#
# def check(target):
#     stack = []
#     for i in target:
#         if i == "(":
#             stack.append(i)
#         elif i == ")":
#             if len(stack) == 0:
#                 return False
#             else:
#                 stack.pop()
#     if len(stack) == 0:
#         return True
#     else:
#         return False
#
# def reverse(target):
#     result = ""
#     for i in target:
#         if i == "(":
#             result += ")"
#         else:
#             result += "("
#     return result
#
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))