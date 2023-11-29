t = int(input())

for _ in range(t):
    s1 = input()
    s2 = input()
    qc = 0
    for i in range(len(s1)):
        
        if s1[i]!='?' and s2[i]!='?':
            if s1[i] != s2[i]:
                print("No")
                qc = 0
                break
            else:
                qc +=1
        elif s1[i]=='?' or s2[i]=='?':
            qc +=1


    if qc >= 1:
        print("Yes")
