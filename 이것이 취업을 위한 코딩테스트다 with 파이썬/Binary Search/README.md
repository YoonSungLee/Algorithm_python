# Binary Search

---

# 1. 순차 탐색(Sequential Search)

* 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
* 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용
* 최악의 경우 시간 복잡도: O(N)

```python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1    # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
input_data = input().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]  # 찾고자 하는 문자열

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

# 2. 이진 탐색(Binary Search) : 반으로 쪼개면서 탐색하기
* 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
* 3개의 변수 사용: 범위의 시작점 / 끝점 / 중간점
* 찾으려는 데이터와 중간점(middle) 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
* 시간 복잡도: O(logN)
    * 한 단계를 거칠 때마다 확인하는 원소가 평균적으로 절반으로 줄어든다. 즉, 단계마다 2로 나누는 것과 동일하므로 연산 횟수는 log2(N)에 비례한다고 할 수 있다.
* 가급적 외울 것!
* 코딩 테스트의 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다. 따라서 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제에 접근해보길 권한다. 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야 하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다는 점을 기억하자.

```python
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2    # mid = int((start + end) / 2)
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)와 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
```

```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            star = mid + 1
    return None

# n(원소의 개수)와 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
```

# 3. 트리 자료구조
* 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리(Tree) 자료구조를 이용하여 항상 데이터가 정렬되어 있다. 따라서 데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, 이진 탐색과 유사한 방법을 이용해 탐색을 항상 빠르게 수행하도록 설계되어 있어서 데이터가 많아도 탐색하는 속도가 빠르다.
* 트리는 부모 노드와 자식 노드의 관계로 표현된다.
* 트리의 최상단 노드를 루트 노드라고 한다.
* 트리의 최하단 노드를 단말 노드라고 한다.
* 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
* 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

# 4. 이진 탐색 트리
* 부모 노드보다 왼쪽 자식 노드가 작다.
* 부모 노드보다 오른쪽 자식 노드가 크다.
* 공식에 따라 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문한다. 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 ㅇ벗는 것이다.

# 5. 빠르게 입력받기
* 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받울 수 있다.
* 이처럼 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
* 관행적으로 외워서 사용하자!

```python
import sys
# 하나의 문자열 데이터 입력받기
# rstrip(): 소스코드에 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위해 사용
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)
```