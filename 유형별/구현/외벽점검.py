# 완전탐색(백 트래킹), 그리디
# https://programmers.co.kr/learn/courses/30/lessons/60062

"""
    초기 아이디어
    최소숫자로 시작해서 안될때마다 한명씩 늘려보기 
    1. dist 역순으로 정렬해서 맨 앞에 원소부터 가능 여부 체크해보기, 안되면 +1씩 개수 늘리는거
    2. 각 사람 수만큼 나타날 수 있는 취약지점간의 조합을 생각한 후 거리 비교 

    해설 아이디어
    
"""

    # 1명인 경우 -> 최대 길이
    # 2명인 경우 -> 일단 두 조합을 나누고, 걔네끼리 나오는 길이중 제일 거리가 짧은 조합 구해서 그게 감당가는한지 확인
    # 3명인 경우 -> 일단 세 조합을 나누고, . . . 

from itertools import combinations

def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse = True)
  
    # weak L,R로 나누기 
    n_L = []
    n_R = []
    for i in weak:
        if i <= n/2:
            n_L.append(i)
        else:
            n_R.append(i)

    # 사람 수만큼 while문 돌려보기 
    while answer <= len(dist):
        answer += 1                     # 일단 1명부터 시작 
        # 1명인 경우
        dis = n_L[-1] + (n - n_R[-1])   # 
        if dis <= dist[0]:
            return answer

        answer += 2
        # 2이상인 경우 
        
        # 조합을 어떻게 만들지도 고민 


        return answer

    return -1


def main():
    print(solution())



if __name__ == '__main__':
    main()


# 12,[1,5,6,10],[1,2,3,4]
# 12,[1,3,4,9,10],[3,5,7]