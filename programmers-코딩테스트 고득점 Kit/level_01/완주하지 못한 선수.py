# 10 min

# my sol
def solution(participant, completion):
    participant.sort()
    completion.sort()
    cut = len(completion)
    idx = 0
    while True:
        if idx == cut or participant[idx] != completion[idx]:
            return participant[idx]
        idx += 1



# other sol
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]



# other sol
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer



# review
def solution(participant, completion):
    hash_list = {}
    count = 0
    for person in participant:
        hash_list[hash(person)] = person
        count += hash(person)
    for person in completion:
        count -= hash(person)

    return hash_list[count]