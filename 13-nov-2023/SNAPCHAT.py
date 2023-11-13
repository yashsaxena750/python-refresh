# cook your dish here
T = int(input())

for tc in range (T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = 0
    D = 0
    for i in range (N):
        if(A[i] != 0 and B[i] != 0):
            C += 1
            if (C>D):
                D = C
        else:
            C = 0
    print(D)