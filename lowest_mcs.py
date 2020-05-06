import numpy as np


def calculate(B, M):
    print("RB allocation through lowest MCS selection")
    count = 0
    B_status = np.zeros(len(B),dtype='int32')
    M.sort(reverse=True)
    lowest_mcs_level = min(B)
    B_status = B_status.tolist()

    for m in M:
        if lowest_mcs_level * len(B) <= m:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
        else:
            flag = False
            for n in range(len(B)):
                if n * lowest_mcs_level >= m and n <= B_status.count(0):
                    print("{} RB's with mcs {} was used to achieve data rate of {}".format(n, lowest_mcs_level, m))
                    count += n
                    for p in range(n):
                        B_status[p] = 1
                        flag = True
                    break
            if not flag:
                print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))

    return count
