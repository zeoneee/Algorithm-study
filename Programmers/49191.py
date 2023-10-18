# 내가 이긴 애들한테 진 애들은 다 내가 이긴 애들이 된다.

def solution(n, results):
    answer = 0
    
    # board 초기화
    board = [[0]*n for _ in range(n)] 
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
    
    # 중간지점 검색
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1
                     
    for i in range(n):
        if board[i].count(0) == 1:
            answer += 1
            
    return answer