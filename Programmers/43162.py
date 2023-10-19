def solution(n, computers):
    answer = 0
     
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if computers[i][k] == 1 and computers[k][j] == 1:
                    computers[i][j] = 1
                    computers[j][i] = 1
    
    visited = [False]*(n+1)
    for i,computer in enumerate(computers):
        if visited[i] == False:
            answer += 1
            visited[i] = True
            for i,v in enumerate(computer):
                if v == 1:
                    visited[i] = True
    
    return answer