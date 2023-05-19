def solution(answers):
    cnt = [[0,1],[0,2],[0,3]]
    submit = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    # answers 길이 이상만큼 제출한답 만들어주기
    for i in range(3):
        temp_l = len(submit[0])
        submit[i] = submit[i]*(len(answers)//temp_l)
        for j in range((len(answers)%temp_l)):
            submit[i] + submit[j]
    
    # 답 검사하기
    for i,v in enumerate(answers):
        for j in range(3):
            if v == submit[j][i]:
                cnt[j][0] += 1   
    
    # max 값 찾기
    cnt.sort(reverse=True)
    answer = [cnt[0][1]]
    
    if cnt[0][0] == cnt[1][0]:
        answer.append(cnt[1][1])
        if cnt[1][0] == cnt[2][0]:
            answer.append(cnt[2][1])
            
    answer.sort()   
    
    return answer