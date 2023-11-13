t = int(input())

for _ in range(0,t):
    n , fr = map(int,input().split())
    sum = 0
    lifr = list(map(int,input().split()))
    lipr = list(map(int,input().split()))
    for i in range(n):
        if lifr[i]>= fr:
            sum += lipr[i]
    
    print(sum)