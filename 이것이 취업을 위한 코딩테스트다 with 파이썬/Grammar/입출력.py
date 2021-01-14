# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

# 입력의 개수가 많은 경우
# rstrip(): readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문제를 제거하기 위함
import sys
data = sys.stdin.readline().rstrip()

# sys.stdin.readline()으로 입력받은 후 데이터를 쪼개어 int형으로 변환한 list를 추출할 경우
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# f-string 문법
answer = 7
print(f'정답은 {answer}입니다.')

# 2차원 배열 입출력(lecture)
'''
3
4
0 0 0 0
0 0 0 0
0 0 0 0
'''
n = int(input())    # 3
m = input(input())  # 4
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

'''
[[0 0 0 0],
 [0 0 0 0],
 [0 0 0 0]]
'''