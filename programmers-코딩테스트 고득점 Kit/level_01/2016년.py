# 6 min

# my sol
def solution(a, b):
    check = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    arr = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = sum(check[:(a-1)]) + b
    return arr[(days % 7) - 1]