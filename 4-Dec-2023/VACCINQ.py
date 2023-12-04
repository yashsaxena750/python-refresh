t = int(input())

for _ in range(t):
    c, p, x, y = map(int, input().split())
    pq = list(map(int,input().split()))
    time = 0

    for i in range(0,p):
        if pq[i] == 0:
            time += x
        else:
            time += y

    print(time)


