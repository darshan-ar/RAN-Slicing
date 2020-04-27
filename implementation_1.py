import numpy as np

#Calculations for 1 TTI
B1 = np.random.randint(1,10,(4,4))
B2 = np.random.randint(1,10,(4,4))
B3 = np.random.randint(1,10,(4,4))

B = np.concatenate((B1,B2,B3),axis=1)
c_max=np.amax(B)
B_status= np.zeros(np.shape(B))
M=2
M1=8
M2=25
MR=[M1,M2]
MR.sort(reverse=True)
#print(B,B_status)

for m in MR:
    for c in reversed(range(29)):
        if c in B:
            n=np.count_nonzero(B==c)
            t = np.argwhere(B == c)
            if c >= m and (B_status[k[0]][k[1]] ==0 for k in t):
                for z in t:
                    if B_status[z[0]][z[1]] ==0:
                        B_status[z[0]][z[1]] = 1
                        break
                print("1 RB allocated for MVNO with bit rate req ", m)
                break
            elif n>1:
                for x in range(n):
                    flag=False
                    if x*c>=m:
                        print("{} RBs with mcs {} allocated for MVNO  with bit rate requirements {}".format(x,c,m))
                        flag=True
                        for p in range(x):
                            #print(p,t)
                            B_status[t[p][0]][t[p][1]]=1
                        break
                if flag==True:
                 break
            else:
                print("No Rbs found for MCS "+str(c)+" for MVNO with bit rate "+str(m))


