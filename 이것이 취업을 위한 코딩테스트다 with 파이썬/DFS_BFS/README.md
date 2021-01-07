# DFS/BFS

---

# 1.자료구조 기초
* 탐색(Search): 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
* 자료구조(Data Structure): 데이터를 표현하고 관리하고 처리하기 위한 구조
* 삽입(Push): 데이터를 삽입한다.
* 삭제(Pop): 데이터를 삭제한다.
* 오버플로(Overflow): 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
* 언더플로(Underflow): 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생



# 2. 스택(Stack)
* 후입선출(Last in First Out)
* 입구와 출구가 동일한 형태
```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)

print(stack)    # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력
```



# 3. 큐(Queue)
* 대기 줄
* 선입선출(First in First out)
```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
# 데이터를 넣고 뺴는 속도가 리스트 자료형에 비해 효율적
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력
```



# 4. 재귀 함수
* 자기 자신을 다시 호출하는 함수
* 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.
* 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.
* 컴퓨터의 구조 측면에서 보자면 연속해서 호출되는 함수는 메인 메모리의 스택 공간에 적재되므로 재귀 함수는 스택 자료구조와 같다는 말은 틀린 말이 아니다.

```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```
<br>

재귀 함수의 종료 조건
```python
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)
```
<br>

2가지 방식으로 구현한 팩토리얼 예제
```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursiver(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursiver(n - 1)
```



# 5. 인접 행렬과 인접 리스트
## 인접 행렬(Adjacency Matrix)
* 2차원 배열로 그래프의 연결 관계를 표현하는 방식
* 파이썬에서는 2차원 리스트로 구현 가능
* 메모리 측면) 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.
* 속도 측면) 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 빠르다.
```python
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표시
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
```

## 인접 리스트(Adjacency List)
* 리스트로 그래프의 연결 관계를 표현하는 방식
* '연결 리스트'라는 자료구조를 이용해 구현
* 2차원 리스트를 이용하여 구현 가능
* 메모리 측면) 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.
* 속도 측면) 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.
```python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)
```



# 6. DFS(Depth-First Search)
* 깊이 우선 탐색
* 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘
* 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작
* stack 자료구조 이용
* 탐색: O(N) (N: 데이터의 개수)

## 원리
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
* 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```



# 7. BFS(Breath First Search)
* 너비 우선 탐색
* 가까운 노드부터 탐색하는 알고리즘
* queue 자료구조 이용
* 탐색: O(N) (N: 데이터의 개수)
* 참고로, 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.

## 원리
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

* 코딩 테스트에서 탐색 문제를 보면 그래프 형태로 표현한 다음 풀이법을 고민하도록 하자.