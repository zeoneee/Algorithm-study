# bfs(최단거리)
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    
    dx=[+1,0,0,-1]
    dy=[0,+1,-1,0]
    stack = [(0,0)]
    
    while stack:
        x,y = stack.pop(0)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                stack.append((nx,ny))

    answer = maps[n-1][m-1]
    return answer if answer > 1 else -1