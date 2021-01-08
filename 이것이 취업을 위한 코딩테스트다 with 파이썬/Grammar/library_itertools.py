# permutations(순열)
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모둔 경우를 계산
# permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import permutations

data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))    # 모든 순열 구하기

print(result)



# combinations(조합)
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import combinations

data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합 구하기

print(result)



# product(중복 순열)
# 서로 다른 n개에서 r개를 중복을 허락하여 뽑은 뒤 일렬로 나열하는 경우의 수
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
# 원소를 중복하여 뽑는다.
# product 객체를 초기화 할 때에는 뽑고자 하는 데이터의 수를 repeat 속성으로 넣어준다.
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import product

data = ['A', 'B', 'C']  # 데이터 준비
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)



# combinations_with_replacement(중복 조합)
# 서로 다른 n개에서 r개를 중복을 허락하여 뽑는 경우의 수
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산
# 원소를 중복해서 뽑는다.
# combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations_with_replacement(data, 2))   # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result)