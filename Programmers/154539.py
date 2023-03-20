def solution(numbers):
    answer = []
        
    for i in range(len(numbers)):
        test = 0
        for j in range(i+1,len(numbers)):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                test=1
                break
        if test==0:
            answer.append(-1)
    
    return answer