def solution(n, words):
    answer = [0,0]
    temp = []
   
    for i,v in enumerate(words):
        if v in temp:
            return [(i+1)%n if (i+1)%n > 0 else n, i//n+1] 
        else:
            if len(temp) == 0:
                temp.append(v)
            elif temp[-1][-1] == v[0]:
                temp.append(v)
            else:
               return [(i+1)%n if (i+1)%n > 0 else n, i//n+1] 

    return answer
