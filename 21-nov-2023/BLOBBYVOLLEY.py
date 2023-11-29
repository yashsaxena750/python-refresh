t = int(input())

for _ in range(t):
    size = int(input())
    ws = input()
    server = 'A'

    sp = 0
    cp = 0

    for i in ws:

        if i == 'B' and server=='B':
            cp +=1#1
            server = 'B'
        elif i == 'A' and server=='A':
            sp +=1#
            server = 'A'
        elif i == 'B' and server == 'A':
            server = 'B'
            cp += 0#0
        elif i == 'A' and server == 'B':
            server = 'A'
            sp +=0 #
    
    print(sp,cp)
