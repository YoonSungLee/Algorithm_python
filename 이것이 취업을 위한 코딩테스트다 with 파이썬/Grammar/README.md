# Code Skill

---

# 순서가 존재하는 데이터에 대하여 순서 및 값을 활용하고자 할 때
dict type보다 list type을 사용하여 index를 순서로 활용한다.

```python
data = [...]
array = [0] * 11
for x in data:
    array[x] += 1
```

# 특정 조건을 가진 정렬
```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age


# return: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
Reference) 정렬 HOW TO [[link]](https://docs.python.org/ko/3/howto/sorting.html)



# 파이썬에서 리스트 크기
int 자료형 데이터의 개수에 따른 메모리 사용량

|데이터의 개수(리스트의 길이)|메모리 사용량|
|---|---|
|1,000|약 4KB|
|1,000,000|약 4MB|
|1,000,000,000|약 40MB|



# 채점 환경
파이썬 3.7로 코드를 작성할 때, 자신의 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하고 문제를 풀면 실행 시간 제한에 안정적이다.<br>
시간 제한이 1초이고, 데이터의 개수가 100만 개인 문제가 있다면 일반적으로 시간 복잡도 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야 한다.<br>
실제로 N = 1,000,000일 때 Nlog2(N)은 약 20,000,000이기 때문이다.<br>
따라서 알고리즘 문제를 풀 때는 시간 제한과 데이터의 개수를 먼저 확인한 뒤에 이 문제를 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있을 것인지 예측할 수 있어야 한다.



# 2중 for문 빠져나가기
boolean type의 새로운 변수 삽입
```python
break_point = 2
breaker = False
for i in range(5):
    for j in range(5):
        if i == break_point and j == break_point:
            breaker = True
            break
    if breaker = True:
        break
```
Reference) 2중 for문 break [[link]](https://gomguard.tistory.com/190)




# iterable
* iterable 객체: 반복 가능한 객체
* 대표적으로 iterable한 타입: list, dict, set, str, bytes, tuple, range
Rerence) Iterable 과 Iterator [[link]](https://wikidocs.net/16068)



# string 정렬 vs list 정렬
```python
# string
a = 'DBAC'
''.join(sorted(a))

# list
b = ['D', 'B', 'A', 'C']
b.sort()
```



# 지도를 리스트로 표현할 때
(1, 1)부터 시작하고 0의 index를 갖는 데이터들의 활용도가 없을 때(예: 벽으로 막혀져 있다) (0, 0)부터 제어하는 것보단 다음과 같은 방법이 직관적일 수 있다.<br>
가로 및 세로 크기를 1씩 늘린 list를 생성 후 (1, 1)부터 제어하는 방식을 사용한다.