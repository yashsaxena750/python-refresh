t = int(input())

for _ in range(t):
    ah = 0
    rc = int(input())
    asc = list(map(int,input().split()))
    bsc = list(map(int,input().split()))

    for i in range(rc):
        if asc[i] <= 2*bsc[i] and bsc[i] <= 2*asc[i]:
            ah +=1

    print(ah)
