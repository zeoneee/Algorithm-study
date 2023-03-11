# 완두콩의 세대와 해당 세대에서 몇 번째 개체인지 알면 형질을 바로 계산하는 프로그램
# 중첩리스트 

"""
    Beans[0] = ["Rr"]
    Beans[1] = ["RR","Rr","Rr","rr"]
    Beans[2] = ["RR","RR","RR","RR","RR","Rr","Rr","rr", ...]
"""

def solution(queries): # queries는 [[n,p]] 형태
    
    answer = []
    for q in queries:
        n = q[0]
        p = q[1]
        
        # 각 n,p마다 형질 값 찾아서 answer에 저장
        Beans = []
        for i in range(n):
            if i == 0:  # 1행
                Beans.append(["Rr"])
            elif i == 1: # 2행
                    #bean = Beans[0][0]
                    beans = ["RR","Rr","Rr","rr"]  # Beans에 append될 리스트
                    Beans.append(beans)
            else: # n행
                beans = []
                for j in range(len(Beans[i-1])):
                    bean = Beans[i-1][j]
                    if bean == "RR":
                        beans.append("RR")
                        beans.append("RR")
                        beans.append("RR")
                        beans.append("RR")
                    elif bean == "Rr":
                        beans.append("RR")
                        beans.append("Rr")
                        beans.append("Rr")
                        beans.append("rr")
                    elif bean == "rr":
                        beans.append("rr")
                        beans.append("rr")
                        beans.append("rr")
                        beans.append("rr")
                Beans.append(beans)
        
        answer.append(Beans[n-1][p-1])
    
    return answer