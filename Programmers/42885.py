# 한번에 최대 두명씩
# 작은애들부터 채우고, i와 i+1번째가 같이 못타게 된 시점부터 한명씩 태우기

def solution(people, limit):
    answer = 0
    people.sort()
    
    for i in range(0,len(people)-1,2):
        if people[i]+people[i+1] <= limit:
            answer += 1
        else:
            answer += len(people)-i
            return answer

    return answer