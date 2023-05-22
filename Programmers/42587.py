
def solution(priorities, location):
    answer = 0
    order = []
    key = priorities[location]
    
    for i,v in enumerate(priorities):
        order.append((v,i))
            
    while order:
        max_v = max(order)
        p = order.pop(0)
        
        if p[0] == max_v[0]:
            if p[0] == key and p[1] == location:
                answer += 1
                return answer
            else: 
                answer += 1
        else:
            order.append(p)  
    
    return answer