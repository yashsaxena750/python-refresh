t = int(input())

for _ in range(t):
    a,b,c,d,k = map(int,input().split())

    if (a+b+c+d)%k==0:
        print("yes")
    else:
        print("no")