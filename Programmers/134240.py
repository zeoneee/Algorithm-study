def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    
    temp = list(answer)
    temp.sort(reverse=True)
    
    answer += '0'
    
    for s in temp:
        answer += s
    
    return answer