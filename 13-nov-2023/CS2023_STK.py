for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    om_count = 0
    addy_count = 0
    om_streak = om_count
    addy_streak = addy_count
    for i in range(n):
        if a[i] != 0:
            om_count += 1
        else:
            om_count = 0
            
        if b[i] != 0:
            addy_count += 1
        else:
            addy_count = 0
        om_streak = max(om_count, om_streak)
        addy_streak = max(addy_count, addy_streak)
        
    if om_streak > addy_streak:
        print("Om")
    elif om_streak < addy_streak:
        print("Addy")
    else:
        print("Draw")