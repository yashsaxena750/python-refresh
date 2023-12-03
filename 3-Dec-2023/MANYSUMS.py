import itertools
t = int(input())

for _ in range(t):
    L,R = map(int,input().split())

    print( ((R+R) - (L+L)) + 1  )
