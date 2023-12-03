# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    date = input()
    n1, n2, _ = date.split('/')
    n1, n2 = map(int, (n1, n2))
    if n1 > 12 and n2 in range(1, 13):
        print("DD/MM/YYYY")
    elif n1 in range(1, 13) and n2 > 12:
        print("MM/DD/YYYY")
    else:
        print("BOTH")
