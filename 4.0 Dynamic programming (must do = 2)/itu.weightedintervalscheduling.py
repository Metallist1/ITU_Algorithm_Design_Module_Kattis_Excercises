import sys
sys.setrecursionlimit(150000)
total_amount = int(input())

input_array = [[-1 for _ in range(3)]
               for _ in range(total_amount)]

M = [-1 for i in range(total_amount)]

for i in range(total_amount):
    word = input().strip().split()  # [0] start [1] end [2] weight
    newW = [int(x) for x in word]
    input_array[i] = newW

input_array = sorted(input_array, key=lambda x: x[1])


def remove_overlap_intervals(current_index):
    low = 0
    high = current_index

    while low <= high:
        mid = int((low + high) / 2)
        if input_array[mid][1] <= input_array[current_index][0]:
            if input_array[mid + 1][1] <= input_array[current_index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1

    return -1


def m_compute_opt(j):
    if j == -1:
        return 0

    if M[j] == -1:
        M[j] = max(input_array[j][2] + m_compute_opt(remove_overlap_intervals(j)),
                   m_compute_opt(j - 1))

    return M[j]


print(m_compute_opt(total_amount - 1))