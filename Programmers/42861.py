# 1. 연결 되어 있는 노드끼리 연결, 길이 갱신해서 비교
#     - 하나만 있는 경우 하나 추가하면됨
# 2. 둘다 리스트에 있을 경우 길이 비교해서 min값 찾기
# 3. 둘다 없을 경우 추가

def solution(n, costs):
    costs.sort()
    visited = []
    
    for cost in costs:
        if len(visited) == 0:
            visited.append([cost[0],cost[1]]) # 연결 노드
            visited.append([cost[2]]) # 연결 노드의 cost
        
        for i in range(0,len(visited),2):
            if cost[0] in visited[i] and cost[1] in visited[i]:
                # 둘다 있을 때
                if sum(visited[i+1]) > cost[2]:
                    visited.append([cost[0],cost[1]])
                    visited.append([cost[2]])
            elif cost[0] in visited[i] or cost[1] in visited[i]:
                # 하나만 있을 때
                if cost[0] in visited[i]:
                    visited[i].append(cost[1])
                else:
                    visited[i].append(cost[0])
                visited[i+1].append(cost[2])
            else:
                # 둘다 없을 때
                visited.append([cost[0],cost[1]]) # 연결 노드
                visited.append([cost[2]]) # 연결 노드의 cost
    
    mincost = 10000
    for i in range(1,len(visited),2):
        if mincost > sum(visited[i]):
            mincost = sum(visited[i])
    
    return mincost 