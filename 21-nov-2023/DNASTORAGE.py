t = int(input())

for _ in range(t):
    n = int(input())
    bstr = input()
    estr = ""
    for i in range(0,n,2):
        if bstr[i] == '0' and bstr[i+1] == '0':
            estr += 'A'
        elif bstr[i] == '0' and bstr[i+1] == '1':
            estr += 'T'
        elif bstr[i] == '1' and bstr[i+1] == '0':
            estr += 'C'
        elif bstr[i] == '1' and bstr[i+1] == '1':
            estr += 'G'
    
    print(estr)
