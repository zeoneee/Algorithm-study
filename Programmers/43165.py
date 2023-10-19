def solution(numbers, target):    
    stack = []
    for number in numbers:
        if not stack:
            stack.append(-number)
            stack.append(number)
        else:
            temp = []
            while stack:
                temp.append(stack.pop())
            for t in temp:
                stack.append(t+number)
                stack.append(t-number)
    
    return stack.count(target)