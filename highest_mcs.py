import numpy as np

def calculate(B,M):
    print("RB allocation through highest MCS selection")
    count = 0
    M.sort(reverse=True)
    highest_mcs = max(B)
    new_B=[i for i in B if i==highest_mcs]
    B_status= np.zeros(len(new_B),dtype='int32')
    B_status=B_status.tolist()
    for m in M:
        if highest_mcs*len(new_B)<=m:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
        else:
            for n in range(len(new_B)):
                print(B_status.count(0))
                if n*highest_mcs>=m and n<=B_status.count(0):
                    print("{} RB's with mcs {} was used to achieve data rate of {}".format(n,highest_mcs,m))
                    count+=n
                    for p in range(n):
                        B_status[p] = 1
                    break
                else:
                    print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
    return count

