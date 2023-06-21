def solution(s):
    answer = 0
    l = len(s)
    s *= 2
    right = True
    
    for i in range(l):
        check = s[i:i+l]
        li = []
        
        for j in check:
            if j == "(" or j == "{" or j=="[":
                li.append(j)
            elif len(li) != 0:
                if j == ")":
                    if li.pop() != "(":
                        right = False
                        break
                elif j == "]":
                    if li.pop() != "[":
                        right = False
                        break
                else:   
                    if li.pop() != "{":
                        right = False
                        break
            else:
                right=False
                        
        if right == False:
            right = True
        else:
            if len(li) == 0:
                answer += 1
        
    return answer