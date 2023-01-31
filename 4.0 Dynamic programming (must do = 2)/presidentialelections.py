import math
import sys

sys.setrecursionlimit(150000)

total_amount = int(input())

input_array = []

total_districts = [[-1 for _ in range(5)]
                   for _ in range(total_amount)]

min_target = 0
max_delegates = 2016

for i in range(total_amount):
    word = input().strip().split()  # [0] weight [1] my people [2] others [3] remaining voters
    newW = [int(x) for x in word]

    min_target = min_target + newW[0]

    total_districts[i][0] = newW[0]
    total_districts[i][1] = newW[1]
    total_districts[i][2] = newW[2]
    total_districts[i][3] = newW[3]

    # cost = total_votes/2 - votes_we_have +1
    total_districts[i][4] = int((newW[1] + newW[2] + newW[3]) / 2) - newW[1] + 1

min_target = int(min_target / 2) + 1

# create a grid. row = amount of districts , column -> amount of delegates
M = [[float('inf') for _ in range(max_delegates + 1)] for _ in range(total_amount + 1)]

# Default the first value
M[0][0] = 0

# for each district
for i in range(total_amount):
    # for each delegate in district
    for j in range(max_delegates+1):
        # check if value is not infinite
        if not math.isinf(M[i][j]):
            # set the next delegates value by comparing the current one to next (since most will be inf. This will set normal values)
            M[i + 1][j] = min(M[i + 1][j], M[i][j])
            # if total cost > than possible voters
            if total_districts[i][4] > total_districts[i][3]:
                M[i + 1][j + total_districts[i][0]] = M[i + 1][j + total_districts[i][0]]
            # if total cost <= 0 and delegate + value < 2016. We assign a new minimum for the next delegate.
            elif total_districts[i][4] <= 0 and j + total_districts[i][0] <= 2016:
                M[i + 1][j + total_districts[i][0]] = min(M[i + 1][j + total_districts[i][0]], M[i][j])
                # if total cost <= 0 and delegate + value < 2016
            elif j + total_districts[i][0] <= 2016:
                M[i + 1][j + total_districts[i][0]] = min(M[i + 1][j + total_districts[i][0]],
                                                          M[i][j] + total_districts[i][4])

min_value = float('inf')
for i in range(min_target, max_delegates+1):
    min_value = min(min_value, M[total_amount][i])

if math.isinf(min_value):
    print("impossible")
else:
    print(min_value)
