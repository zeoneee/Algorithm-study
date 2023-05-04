# bruteforce

# dfs로 다시
# 최적부분구조로 다시

from itertools import permutations
def solution(ability):
    answer = 0
    
    # 각 열조합별로 max값 뽑아서 합계를 구한  제일 큰 값으로 return 
    # 열조합 구하기(순열)
    index_list = [i for i in range(len(ability[0]))]
    index_permutations = []
    for i in permutations(index_list,len(index_list)):
        index_permutations.append(i)
    
    # 열조합 별로 max값 뽑아서 합계 
    for idx in index_permutations:  # 열조합별
        idx_row = [i for i in range(len(ability))] # 해당 행 list(max값 나온 idx는 pop해야하니까)
        sum_power = 0
        for j in idx: # 해당 열별로
            power_max = 0
            max_idx = 0
            for i in idx_row: # 해당 행의 max값
                if ability[i][j] > power_max:
                    power_max = ability[i][j]
                    max_idx = i
            idx_row.remove(max_idx) # max값 idx 삭제
            sum_power += power_max
                
        if sum_power > answer:
            answer = sum_power
    
    return answer

    