def solution(progresses, speeds):
    answer = []
    completed = []
    
    # 완료일 계산
    for i,v in enumerate(progresses):
        day = (100-v) // speeds[i]
        if (100-v) % speeds[i] > 0:
            day += 1
        completed.append(day)
    
    temp = cnt = 0
    
    while completed:
        c = completed.pop(0)
        if temp >= c: # 앞 작업이 아직 안 끝난 경우
            cnt += 1
        else: 
            answer.append(cnt)
            temp = c
            cnt = 1
    
    answer.append(cnt)
    answer.pop(0) # cnt=0 들어간 경우 빼주기
            
    return answer