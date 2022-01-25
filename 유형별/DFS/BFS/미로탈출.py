from collections import deque # BFS

n,m = map(int,input().split())
data = [list(map(int,list(input()))) for _ in range(n)]

# 이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 구현
def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # -> 인접 좌표를 계속 추가하고 / queue 방식대로 first out해서 탐색 
    # queue가 빌 때 까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어났으면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽이면 무시
            if data[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny)) # -> 여기서 queue로 돌아가서 반복 
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return data[n-1][m-1] # 왜냐면 계속 그 거리만큼 +1해서 왔으니까

print(bfs(0,0)) 

