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


