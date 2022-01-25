# n,m 입력
n,m = map(int,input().split())

# 2차원 리스트 맵 정보 입력
data = [list(map(int,list(input()))) for _ in range(n)] # n,m 모양 행렬 한번에 받는 코드

"""
DFS 이용
data[i]랑 data[i+1]이랑 같으면 계속 직진, 다르면 탈락 

1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤 주변 지점 중 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문 진행
3. 1,2번의 과정을 반복하며 방문하지 않은 지점의 수를 count
"""

# dfs로 방문 -> 1. 종료조건 2.방문체크 3.재귀호출
def dfs(x,y):
    # 주어진 범위를 벗어나면 즉시 종료(1)
    if x <= -1 or x >= n or y <= -1 or y>=m: # 행렬에서의 위치를 x,y로 표현
        return False
    # 현재 노드를 아직 방문하지 않았다면(2)
    if data[x][y] == 0:
        data[x][y] =1 # 방문처리
        # 상하좌우 재귀호출(3)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # -> 쭉쭉쭉 가서 다 인접하면 True고
    return False # 인점 x인 곳이 걸리면 False고 

# 모든 노드에 대해 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        # 현재위치에서 dfs 수행 -> 이 지점에서 상하좌우했을 때 0인 지점 있는가 check
        if dfs(i,j) == True:
            result += 1

print(result)
    



