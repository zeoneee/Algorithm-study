def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
                
    if len(stack) != 0: # 괄호 다 안 닫힌 경우
        return False
    
    return True