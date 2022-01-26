# map의 크기 입력
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]   # n x m 행렬

# 캐릭터 위치, 방향 입력
x,y,direction = (map(int,input().split()))
d[x][y] = 1 # 현재 좌표 방문 처리

# 맵 정보 입력
data = [list(map(int,list(input()))) for _ in range(n)]

# 방향 설정 (북동남서 --> 근데 why?)
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

# 왼쪽으로 회전 (반시계방향)
def turn_left():
    global direction # 정수형 변수 direction변수가 함수 바깥에서 선언된 전역변수이기 때문
    direction -= 1
    if direction == -1:
        direction = 3

# 매뉴얼 대로 캐릭터 이동
cnt = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if data[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있다면 종료
        else:
            break
        turn_time = 0

print(cnt)