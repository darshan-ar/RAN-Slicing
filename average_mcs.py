import numpy as np
import math
#Calculations for 1 TTI
B1 = np.random.randint(1,10,(4,4))
B2 = np.random.randint(1,10,(4,4))
B3 = np.random.randint(1,10,(4,4))

B = np.concatenate((B1,B2,B3),axis=1)
B1=B.tolist()
B1 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9]
c_max=np.amax(B)

M=2
M1=8
M2=60
MR=[M1,M2]
MR.sort(reverse=True)
print(sorted(B1),math.floor(sum(B1)/len(B1)))

average_mcs= math.floor(sum(B1)/len(B1))
new_B1=[i for i in B1 if i>=average_mcs]
B_status= np.zeros(len(new_B1))
B_status=B_status.tolist()
print(new_B1)

for m in MR:
    if average_mcs*len(new_B1)<=m:
        print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
    else:
        for n in range(len(new_B1)):
            if n*average_mcs>=m and n<=B_status.count(0):
                print("{} RB's with mcs {} was used to achieve data rate of {}".format(n,average_mcs,m))
                for p in range(n):
                    B_status[p] = 1
                break



