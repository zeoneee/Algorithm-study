"""
    모든 프로그램들이 종료되는 시각 / 프로그램의 점수마다 대기시간의 합
    [프로그램 우선순위, 프로그램이 호출된 시각, 프로그램의 실행 시간]
"""

from queue import PriorityQueue
def solution(program):
    answer = [0 for i in range(11)] # answer[0] = 실행시간의 합 
    
    time_queue = PriorityQueue() # 실행순서 기준 queue
    for i in program:
        time_queue.put(i)
        
    priority_queue = PriorityQueue() # 우선순위 기준 queue
    
    now_time = 0 
    # 실행시간 기준 queue가 다 처리될 때까지 
    # 실행시간에 따라 priority_queue 넣기. -> 어떻게?
    while len(time_queue) != 0:
        
        pro = time_queue.get()[1]
        priority_queue.put(pro)
    
        process = priority_queue.get()[0]
        if process[1] > now_time:
            # 실행 
            answer[process[0]] += now_time # 대기시간 add
            now_time += process[2]
        else:   # pop한 process가 현재 시간에 실행되지 못하는 경우 
            

        now_time += 1
        
        
    return answer



import heapq

def solution(program):
answer = [0] * 11

less
Copy code
pq = []
pq2 = []

for i in range(len(program)):
    temp = [program[i][0], program[i][1], program[i][2]]
    heapq.heappush(pq, temp)
    
    temp = pq[0]

nowtime = 0

while pq or pq2:
    v = []
    
    while pq:
        v = heapq.heappop(pq)
        if v[1] > nowtime:
            break
        heapq.heappush(pq2, v)
    
    if not pq2:
        v = heapq.heappop(pq)
        nowtime = v[1] + v[2]
    else:
        v = heapq.heappop(pq2)
        if nowtime > v[1]:
            answer[v[0]] += (nowtime - v[1])
            nowtime += v[2]
        else:
            nowtime += v[2]

answer[0] = nowtime

return answer