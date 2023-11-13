t = int(input())

for _ in range(t):
    sum = 0
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    large = arr[n-1]
    for i in range(1,n):
        if large > arr[n-(i+1)]:
            sum = large + arr[n-(i+1)]
            break

    print(sum)
    
