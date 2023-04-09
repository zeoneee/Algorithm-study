def solution(operations):
    answer = []
    
    for operation in operations:
        o,v = operation.split()
        if o == "I":
            answer.append(int(v))
        elif o == "D":
            if len(answer) == 0:
                continue;
            else:
                answer.sort()
                if v == "-1":
                    answer.pop(0)
                else:
                    answer.pop(-1)
        
    if len(answer) == 0:
            return [0,0]
    else: return [max(answer),min(answer)]    