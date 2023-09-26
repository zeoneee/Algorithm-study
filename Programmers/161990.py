#시작:[제일위,제일왼], 끝:[제일아래,제일오른쪽]
def solution(wallpaper):
    answer = [99,99,-1,-1]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < answer[0]:
                    answer[0] = i
                if j < answer[1]:
                    answer[1] = j
                if i > answer[2]:
                    answer[2] = i
                if j > answer[3]:
                    answer[3] = j
    
    answer[2] += 1
    answer[3] += 1
    return answer