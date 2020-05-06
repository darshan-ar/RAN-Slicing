import numpy as np

#Calculations for 1 TTI
B1 = np.random.randint(1,10,(4,4))
B2 = np.random.randint(1,10,(4,4))
B3 = np.random.randint(1,10,(4,4))

B = np.concatenate((B1,B2,B3),axis=1)
B1=B.tolist()
B1 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9]
c_max=np.amax(B)
B_status= np.zeros(len(B1))
M=2
M1=8
M2=60
MR=[M1,M2]
MR.sort(reverse=True)
print(sorted(B1))
lowest_mcs = min(B1)
B_status=B_status.tolist()

for m in MR:
    if lowest_mcs*len(B1)<=m:
        print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
    else:
        flag=False
        for n in range(len(B1)):
            if n*lowest_mcs>=m and n<=B_status.count(0):
                print("{} RB's with mcs {} was used to achieve data rate of {}".format(n,lowest_mcs,m))
                for p in range(n):
                    B_status[p] = 1
                    flag=True
                break
        if flag!=True:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))

