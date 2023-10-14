def solution(n):
    answer = []
    
    def hanoi(src,des,mid,n):
        if n==1:
            print("1, append",[src,des])
            answer.append([src,des])
        else:
            #1~n-1번째: 1->3->2
            print(1,src,"->",des,"->",mid,n-1)
            hanoi(src,mid,des,n-1)
            #n번째: 1->3
            print("2, append",[src,des])
            answer.append([src,des])
            #1~n-1번째: 2->3
            print(3,mid,"->",src,"->",des)
            hanoi(mid,des,src,n-1)
    
    hanoi(1,3,2,n)
    return answer

def main():
    print(solution(4))

if __name__ == '__main__':
    main()