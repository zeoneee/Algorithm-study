# https://programmers.co.kr/learn/courses/30/lessons/60061
# 시뮬레이션 
# build_frame의 원소는 [x,y,a,b] a: 0은 기둥, 1은 보, b: 0은 삭제, 1은 설치


# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 게 기둥이라면 : 1. 바닥 위, 2. 보의 한쪽 끝부분 위, 3. 다른 기둥 위 
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: # 바닥, 왼쪽 보, 오른쪽 보, 기둥 위
                continue
            return False # 아니라면 false 반환 
        elif stuff == 1: # 설치된 게 보라면 : 1. 한쪽 끝부분이 기둥 위, 2. 양쪽 끝부분이 다른 보와 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:   # 전체 명령 개수는 최대 1000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x,y,stuff]) # 일단 삭제 ㄱ
            if not possible(answer):
                answer.append([x,y,stuff]) # 가능한 구조물이 아니면 다시 설치
        if operate == 1: # 설치
            answer.append([x,y,stuff]) # 일단 설치 ㄱ
            if not possible(answer):
                answer.remove([x,y,stuff]) # 가능한 구조물이 아니면 다시 삭제

    return sorted(answer)

n = int(input())
build_frame = [list(map(int,list(input()))) for _ in range(n)] # 입력이 잘못됨 
print(solution(n,build_frame))