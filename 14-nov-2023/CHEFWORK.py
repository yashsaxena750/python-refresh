t = int(input())

coins = list(map(int,input().split()))
worker = list(map(int,input().split()))
min_value_1 = float('inf')  # Initialize with a very large number
min_value_2 = float('inf')  # Initialize with a very large number
min_value_3 = float('inf')

for idx, val in enumerate(worker):
    if val == 1:
        min_value_1 = min(min_value_1, coins[idx])
    elif val == 2:
        min_value_2 = min(min_value_2, coins[idx])
    elif val == 3:
        min_value_3 = min(min_value_3,coins[idx])

if (min_value_1+min_value_2 < min_value_3):
    print(min_value_1+min_value_2)
else:
    print(min_value_3)