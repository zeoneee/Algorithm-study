def solution(N, number):
    if number == N:
        return 1
    
    dp = [0]
    for cnt in range(1,9): # cnt가 될 수 있는 수
        partial_set = set()
        partial_set.add(int(str(N)*cnt)) # 이어붙여서 만드는 경우
        for i in range(1,cnt):
            for op1 in dp[i]:
                for op2 in dp[cnt-i]:
                    partial_set.add(op1+op2)
                    partial_set.add(op1*op2)
                    partial_set.add(op1-op2)
                    if op2 != 0:
                        partial_set.add(op1//op2)
        # cnt번째에 만든 집합에서 number가 나온다면 return cnt
        if number in partial_set:
            return cnt
        dp.append(partial_set)
            
    return -1