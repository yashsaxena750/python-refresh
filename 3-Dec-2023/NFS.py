import math

t = int(input())

for _ in range(t):
    u, v, a, s = map(int,input().split())
    res = (u**2 - 2*a*s)
    v = v**2
    if(res > v):
        print("No")
    else:
        print("Yes")
