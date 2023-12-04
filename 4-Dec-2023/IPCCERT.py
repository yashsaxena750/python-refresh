t, mw, qa = map(int,input().split())

for _ in range(t):
    a, b, c, d, e = map(int,input().split())
    cc = 0

    if ( a+b+c+d >= mw or qa<=e ):
        cc += 1

print(cc)
