def main():
    n = int(input())
    m = int(input())
    virus = [[] for _ in range(n+1)]
    
    for _ in range(m):
        x,y = map(int,input().split())
        virus[x].append(y)
        virus[y].append(x)
    
    stack = []
    
if __name__ == "__main__":
    main()