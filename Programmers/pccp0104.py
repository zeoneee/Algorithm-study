"""
    모든 프로그램들이 종료되는 시각 / 프로그램의 점수마다 대기시간의 합
    [프로그램 점수, 프로그램이 호출된 시각, 프로그램의 실행 시간]
    stack
"""
"""
    process:
    먼저 들어온 순으로 정렬
    # 첫번째
    먼저 들어온 애들 stack에 넣고 우선순위 비교
    우선순위 높은 애부터 실행 -> 실행시간 count
    대기 시간 count
    # n번째
    초별로 들어옴 
    stack에 있는 애랑 우선순위 비교 -> 정렬 
    우선순위 높은 애부터 실행 
"""

def solution(program):
    answer = [0 for i in range(11)] # answer[0] = 실행시간의 합 

    # 들어온 시간순으로 정렬
    program.sort(key=lambda x:x[1])
    
   
    return answer