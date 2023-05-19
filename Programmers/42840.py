def solution(answers):
    answer = []
    score = [0,0,0]
    submit = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    for i,v in enumerate(answers):
        if submit[0][i%5] == v:
            score[0] += 1
        if submit[1][i%8] == v:
            score[1] += 1
        if submit[2][i%10] == v:
            score[2] += 1
            
            
    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i+1)
            
    return answer