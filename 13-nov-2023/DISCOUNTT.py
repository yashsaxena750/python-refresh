# cook your dish here
t = int(input())

for _ in range(t):
    n , dc , mc = map(int,input().split())
    plist = list(map(int,input().split()))
    acost = 0
    dcost = 0

    for item in plist:
        acost = acost + item

    for item in plist:

        if item-mc > 0:
            dcost += (item-mc)
    dcost += dc

    if dcost < acost:
        print("COUPON")
    else:
        print("NO COUPON")