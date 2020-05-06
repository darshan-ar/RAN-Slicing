import numpy as np
import random

def calculate(B,M):
    print("RB allocation through random MCS selection")
    count=0
    M.sort(reverse=True)
    random_mcs= random.choice(B)
    new_B=[i for i in B if i>=random_mcs]
    B_status= np.zeros(len(new_B),dtype='int32')
    B_status=B_status.tolist()
    for m in M:
        if random_mcs*len(new_B)<=m:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
        else:
            for n in range(len(new_B)):
                if n*random_mcs>=m and n<=B_status.count(0):
                    print("{} RB's with mcs {} was used to achieve data rate of {}".format(n,random_mcs,m))
                    count+=n
                    for p in range(n):
                        B_status[p] = 1
                    break
    return count




