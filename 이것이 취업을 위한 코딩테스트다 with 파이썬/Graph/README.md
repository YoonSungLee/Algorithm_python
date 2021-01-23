# Graph

---

* 그래프: 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조
    * *서로 다른 개체(혹은 객체, Object)가 연결되어 있을 때*
    * *여러 개의 도시가 연결되어 있을 때*
* 트리: 부모에서 자식으로 내려오는 계층적인 모델

| |그래프|트리|
|---|---|---|
방향성|방향 그래프 혹은 무방향 그래프|방향 그래프|
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|루트 노드가 없음|루트 노드가 존재|
|노드간 관계성|부모와 자식 관계 없음|부모와 자식 관계|
|모델의 종류|네트워크 모델|계층 모델|

* 그래프의 구현 방법
    * 인접 행렬(Adjacency Matrix): 2차원 배열을 사용하는 방식
        * 공간 복잡도: O(V^2)
        * 탐색 시간 복잡도: O(1)
        * 플로이드 워셜 알고리즘에서 사용하는 방식 <-- 노드의 개수가 적은 경우 사용
    * 인접 리스트(Adjacency List): 리스트를 사용하는 방식
        * 공간 복잡도: O(E)
        * 탐색 시간 복잡도: O(V)
        * 다익스트라 최단 경로 알고리즘에서 사용하는 방식 <-- 노드의 개수가 많은 경우 사용
    
# 1. 서로소 집합(Disjoint Sets)
## 서로소 집합
* 서로소 집합: 공통 원소가 없는 두 집합
* 서로소 집합 자료구조(union-find 자료구조): 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
    * union(합집합): 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    * find(찾기): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

## 서로소 집합 계산 알고리즘
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    1. A와 B의 루트 노드 A', B'를 각각 찾는다.
    2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다).
2. 모든 Union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.
* 이렇게 구한하면 답을 구할 수는 있지만, find 함수가 비효율적으로 동작한다. 최악의 경우 find 함수가 모든 노드를 다 확인하는 터라 시간 복잡도가 O(V)라는 점이다.

```python
# 기본적인 서로소 집합 알고리즘 소스 코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연선)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

## 경로 압축(Path Compression) 기법
* find 함수를 아주 간단한 과정으로 최적화하는 기법
* find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법

```python
# 경로 압축 기법 소스코드

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```

## 개선된 서로소 집합 알고리즘
```python
# 개선된 서로소 집합 알고리즘 소스 코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연선)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

## 서로소 집합 알고리즘의 시간 복잡도
* (노드의 개수가 V개이고, 최대 V - 1개의 union 연산과 M개의 find 연산이 가능할 때)
* 시간 복잡도: O(V + M(1 + log_(2 - M/V)_(V)))

## 서로소 집합을 활용한 사이클 판별
* 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징이 있다.
* (참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.)

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    2. 루트 노드가 서로 같다면(Cycle)이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

```python
# 서로소 집합을 활용한 사이클 판별 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False   # 사이클 발생 여부

for i in range(e):
    a, b =map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
```

# 2. 크루스칼 알고리즘
## 신장 트리(Spanning Tree)
* 그래프 알고리즘 문제로 자주 출제되는 문제 유형
* 하나의 그래프가 있을 때 1)모든 노드를 포함하면서 2)사이클이 존재하지 않는(트리의 성립 조건) 부분 그래프

## 크루스칼 알고리즘(Kruskal Algorithm)
* 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리(최소 신장 트리)를 찾는 알고리즘
* 그리디 알고리즘으로 분류
* 먼저 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함
* 이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다.
* 최소 신장 트리: 간선의 개수 = 노드의 개수 - 1

## 크루스칼 알고리즘 순서
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.

```python
# 크루스칼 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```

## 크루스칼 알고리즘의 시간 복잡도
* 시간 복잡도: O(ElogE)
    * 크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분이 간선을 정렬하는 작업이며, E개의 데이터의 정렬했을 때의 시간 복잡도는 O(ElogE)이기 때문이다.
    * 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간복잡도는 정렬 알고리즘의 시간 복잡도보다 작으므로 무시한다.

# 3. 위상 정렬(Topology Sort)
* when) 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
* 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
* 진입차수(indegree): 특정한 노드로 '들어오는' 간선의 개수

## 위상 정렬 알고리즘
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음 과정을 반복한다.
    1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
    
* 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
    * 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것이다.
    * 사이클이 존재하는 경우 사이클에 포함되어 있는 원소 중에서 어떠한 원소도 큐에 들어가지 못하기 때문이다.
    
```python
# 위상 정렬 코드

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    # 진입차수를 1로 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
```

## 위상 정렬의 시간 복잡도
* O(V + E)
* 위상 정렬을 수행할 때는 차례대로 모든 노드를 확인하면서, 해당 노드에서 풀발하는 간선을 차례대로 제거해야 한다.
* 결과적으로 노드와 간선을 모두 확인한다는 측면에서 O(V + E)의 시간이 소요되는 것이다.