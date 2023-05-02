# 정수들은 순서를 바꾸지 않음. +,-만 반복해서 해보면 됨 

def solution(numbers, target):
    idx = curr = 0
    
    def dfs(idx, curr, nums, target):
        # 종료 조건, idx가 nums의 길이에 도달했을 때 
        if idx == len(nums):
            return 1 if curr == target else 0
        
        # +, - 하나씩 해보기
        return dfs(idx+1, curr+nums[idx], nums, target) \
                + dfs(idx+1, curr-nums[idx], nums, target)
    
    answer = dfs(idx, curr, numbers, target)
    return answer