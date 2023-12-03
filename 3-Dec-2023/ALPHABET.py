def read_check():
    strn = input()
    alist = list(strn)
    t = int(input())

    for _ in range(t):
        mstr = input()
        if set(mstr).issubset(set(alist)):
            print("Yes")
        else:
            print("No")

read_check()
