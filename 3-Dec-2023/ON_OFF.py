# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    state = 0
    for i in range(n):
        if(s[i]!=r[i]):
            state=state+1
    if(state%2==0):
        print(1)
    else:
        print(0)