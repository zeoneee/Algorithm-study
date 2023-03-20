def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] # numbers의 index를 저장
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer