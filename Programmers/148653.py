def solution(storey):
    answer = 0
    nums = list(map(int, list(str(storey))))
    nums = [[n,i] for i,n in enumerate(nums)]
    
    while nums:
        n,i = nums.pop()
        if n < 5:
            answer += n
        elif n > 5:
            answer += 10-n
            if i == 0:
                nums.append((1,0)) # 맨 앞자리일 때 오름1 있다면
            else:
                nums[i-1][0] += 1
        else:
            if i == 0 or nums[i-1][0] < 5: # 맨 앞자리 일때
                answer += n 
            else:
                answer += 10-n
                nums[i-1][0] += 1
                
    return answer

# data를 stack화해서 하나씩 pop()하면서 뒷자리부터 검사하는 아이디어 