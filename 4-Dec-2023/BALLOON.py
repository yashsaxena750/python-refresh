t = int(input())

for _ in range(t):
    n = int(input())
    nlist = {1, 2, 3, 4, 5, 6, 7}
    nums = list(map(int, input().split()))
    sc = 0

    for el in nums:
        if el in nlist and len(nlist)>0:
            nlist.remove(el)
            sc +=1
        elif len(nlist)>0:
            sc +=1

    print(sc)

