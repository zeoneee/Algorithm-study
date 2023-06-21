def solution(elements):
    answer = []
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            if len(elements[j:j+i]) == i:
                answer.append(sum(elements[j:j+i]))
            else:
                temp_s = sum(elements[j:j+i])
                l = len(elements[j:j+i])
                temp_s += sum(elements[:i-l])
                answer.append(temp_s)
    
    return len(set(answer))