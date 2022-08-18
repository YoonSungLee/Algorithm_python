# Python Code

## 부동 소수점 표현(p421)

10진수 체계에서는 0.3과 0.6을 더한 값이 0.9로 정확히 떨어지지만, 2진수에서는 0.9를 정확히 표현할 수 있는 방법이 없다. 따라서 소수점 값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 못해서 원하는 결과를 얻지 못할 수 있다. 이럴 때는 round() 함수를 이용할 수 있다.

```python
a = 0.3 + 0.6
print(a)	# 0.899999999999

if a == 0.9:	# False
	print(True)
else:
	print(False)


# round(실수형 데이터, 반올림하고자 하는 위치 - 1)
a = 0.3 + 0.6
print(round(a, 4))	# 0.9

if round(a, 4) == 0.9:	# True
    print(True)
else:
    print(False)
```



## 크기가 N인 리스트 초기화(p421, 423)

```python
# 크기가 N인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)	# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 크기가 N x M인 2차원 리스트 초기화 (잘못된 방법)
# 내부적으로 포함된 4개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다.
n = 3
m = 4
array = [[0] * m] * n
print(array)	# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

array[1][1] = 5
print(array)	# [[0, 5, 0], [0, 5, 0], [0, 5, 0], [0, 5, 0]]


# 크기가 N x M인 2차원 리스트 초기화
# 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다.
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)	# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```



## SORT(p424)

```python
a = [1, 2, 3]

# class의 메서드로 작동
# a 리스트 자체를 바꿔줌
a.sort()

# 내장 함수
# a 리스트 변화 없이 return값만 넘겨줌
sorted(a)
```



## 리스트에서 특정한 값의 원소를 모두 제거하는 방법(p425)

```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 것만을 저장
result = [i for i in a if i not in remove_set]
print(result)	# [1, 2, 4]
```



## 원소 존재 여부 파악 시: list/tuple vs set/dictionary(p431)

특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 list/tuple: O(N), set/dictionary: O(1) 이다.따라서 set 또는 dictionary는 '특정한 데이터가 이미 등장한 적이 있는지 여부'를 체크할 때 매우 효과적이다.

```python
a = [1, 2, 3]
print(1 in a)	# O(N)

a = {1, 2, 3}
print(1 in a)	# O(1)
```



## 리스트는 전역 변수 처럼 사용

리스트는 함수 내에서 global 키워드 없이 접근 가능



## 입력을 위한 전형적인 소스 코드 (p444, 445, 446)

```python
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

# 입력의 개수가 많은 경우
import sys
data = sys.stdin.readline().rstrip()
```



## 2차원 배열 입출력

````python
```
3
4
0 0 0 0
0 0 0 0
0 0 0 0
```

n = int(input())
m = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
````

