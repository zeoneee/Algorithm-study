# 미로탈출.py 참고해서 작성했고, test case는 통과했는데 런타임 에러뜸. 이유를 모르겠음

from collections import deque 

def solution(maps):
        
    # 이동할 네 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y)) # 인접 좌표 추가
            
        # queue가 빌 때 까지 반복
        while queue:
            x,y = queue.popleft()
            # 현재 위치에서 네 방향으로 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 미로 찾기 공간 벗어났으면 무시
                if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                    continue
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny)) # -> 여기서 queue로 돌아가서 반복 
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return maps[4][4] 
    
    answer = bfs(0,0)
    return answer if answer > 1 else -1