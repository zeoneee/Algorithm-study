def solution(s):
    ans, pair = 0,{'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            if v in ['{','[','(']: 
                stack.append(v)
            elif not stack or v != pair[stack[-1]]: 
                iscorrect = False # stack.pop()해서 비교하는거랑 같음
            else: stack = stack[:-1] # 비교했을때 같다면 그대로 pop
        
        ans += int(iscorrect and not stack) # iscorrect가 True고 stack이 true일때
        s = s[1:]+s[0]
    
    return ans