# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1

T = int(input())
answer_list = []

for _ in range(T):
    N = int(input())
    score_list = []
    for _ in range(N):
        score_list.append(list(map(int, input().split())))
    score_list.sort()

    ans = 1     # 가장 첫 번째 사람은 합격이므로 1로 설정
    # 서류 순위가 높은 사람들보다 면접 순위가 높으면 된다.
    # --> 자신의 면접 순위가 min_rank이면 합격
    min_rank = score_list[0][1]
    for i in range(1, N):
        rank = score_list[i][1]
        if rank < min_rank:
            min_rank = rank
            ans += 1
    answer_list.append(ans)

for i in answer_list:
    print(i)



