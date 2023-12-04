# cook your dish here
t = int(input())

for _ in range(t):
    tc, ms, mp = map(int, input().split())
    slist = list(map(int, input().split()))
    mflag = 1
    aflag = 1

    for i in range(0, ms):
        if slist[i] != 1:
            mflag = 0
            print(0)
            break

    if mflag:
        for el in slist:
            if el != 1:
                aflag = 0
                print(mp)
                break

    if mflag and aflag:
        print(100)