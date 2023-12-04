t = int(input())

for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()

    print(m[len(m)-1]-m[0])
