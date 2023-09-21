def solution(arr):
    answer = [0,0]
    stack = [] 
    stack.append(arr.copy()) #stack 활용해서 검사할 것들 쭉 담아놓기
    
    #다 같은 수일 경우 먼저 check
    check = arr[0][0]
    for i in range(len(arr)): 
        for j in range(len(arr)):
            if arr[i][j] != check:
                check = -1
                break
        if check == -1:
            break
    if check != -1:
        answer[check] += 1
        return answer
    
    while stack:
        temp = stack.pop()
        
        #4로 나누는 과정 
        mid = len(temp)//2
        firstXY = [[0,0], [0,mid], [mid,0], [mid,mid]] #4등분 했을 때 검사를 시작할 가장 앞번호
        
        for n in range(4):
            x,y = firstXY[n][0], firstXY[n][1]
            check = temp[x][y] #1 or 0
            for i in range(mid): 
                for j in range(mid):
                    if temp[x+i][y+j] != check:
                        check = -1
                        break
                if check == -1:
                    break
            if check == -1: #압축x, temp에서 slicing해서 stack에 저장
                temp_stack = []
                for i in range(mid):
                    row = temp[x+i][y:y+mid]  # 각 행에서 처음 두 열만 선택
                    temp_stack.append(row)
                stack.append(temp_stack)
                
            else: #압축o
                answer[check] += 1        
    
    return answer
    

def main():
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(arr))

if __name__ == "__main__":
    main()
