#그래프-플로이드와샬 알고리즘
# 1. fares에 있는 지점들 사이의 택시요금 cost를 갱신해주고 floyd_warshall함수를 실행한다.
# 2. floyd_warshall함수: k를 1부터 n번 지점까지 돌면서 i에서 k를 거쳐 j까지 가는 cost를 갱신한다.
# 3. i를 A와 B가 같이가는 지점이라고 가정하고, 1부터 n까지 반복문을 돌며 s에서 i까지 + i에서 a까지 + i에서 b까지의 비용을 구해 ans와 비교해 작은 값을 ans에 넣는다. 모든 지점 확인 후 ans return

def solution(n, s, a, b, fares):
    INF = 200000001
    answer = INF
    cost = [[INF]*(n+1) for _ in range(n+1)]
    
    def floyd_warshall():
        for k in range(1,n+1): #거치는점
            for i in range(1,n+1): #시작점
                for j in range(1,n+1): #끝점
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][k]+cost[k][j], cost[i][j])
                        # print(i,'->',j,'=',cost[i][j])
    # 1->2까지의 경로가 정점의 수만큼(6번) 돌면서 최단거리가 최적화됨: 모든 경우의수를 계산 가능
    
                        
    for i,j,c in fares: #비용초기화
        cost[i][j] = c
        cost[j][i] = c
    floyd_warshall()
    
    # 먼저 모든 지점에서의 최단거리를 계산해놓은 후 start지점에서 a,b까지의 최단거리 계산
    for i in range(1,n+1):
        answer = min(cost[s][i]+cost[i][a]+cost[i][b], answer)
    
    return answer