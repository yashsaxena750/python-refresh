# cook your dish here
for _ in range(int(input())):
    M,x,y=map(int,input().split())
    H=list(map(int,input().split()))
    H.sort()
    Hmin=[H[i]-x*y for i in range(M)]
    Hmax=[H[i]+x*y for i in range(M)]
    s=0
    for j in range(1,101):
        flag=1
        for k in range(M):
            if Hmin[k]<=j<=Hmax[k]:
                flag=0
                break
        if flag:
            s+=1
    print(s)