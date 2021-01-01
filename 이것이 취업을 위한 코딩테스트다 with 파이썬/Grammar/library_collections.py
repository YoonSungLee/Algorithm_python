# deque
# 스택 혹은 큐 자료구조의 대용으로 사용 가능
# 인덱싱, 슬라이싱 등의 기능은 사용 불가
# 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때 매우 효과적을 ㅗ사용
# popleft() / pop()
# appendleft() / append()
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))   # 리스트 자료형으로 변환



# Counter
# 등장 횟수를 세는 기능 제공
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
# 원소별 등장 횟수를 세는 기능이 필요할 때 사용
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter))    # 사전 자료형으로 변환