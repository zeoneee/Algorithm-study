def solution(X, Y):
    answer = ''
    Y = list(Y)
    
    for x in X:
        if x in Y: 
            answer += x
            Y.remove(x)
    
    answer = ''.join(sorted(list(answer),reverse=True))
    if answer == "":
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else: return answer