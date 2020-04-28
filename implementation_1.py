import numpy as np

#Calculations for 1 TTI
B1 = np.random.randint(1,10,(4,4))
B2 = np.random.randint(1,10,(4,4))
B3 = np.random.randint(1,10,(4,4))

B = np.concatenate((B1,B2,B3),axis=1)
B1=B.tolist()
B1 = sum(B1,[])
c_max=np.amax(B)
B_status= np.zeros(len(B1))
M=2
M1=64
M2=60
MR=[M1,M2]
MR.sort(reverse=True)
print(sorted(B1))

for m in MR:
    for c in reversed(range(29)):
        if c in B:
            n=B1.count(c)
            t = [i for i,x1 in enumerate(B1) if x1==c]
            n1 = [x1 for x1 in t if B_status[x1] == 0]
            if c >= m and (B_status[t[0]] ==0):
                B_status[t[0]]=1
                print("1 RB with mcs "+str(c)+" allocated for MVNO with bit rate req ", m)
                break
            elif len(n1)>1:
                flag = False
                for x in range(len(n1)):
                    if x*c>=m:
                        print("Same: {} RBs with mcs {} allocated for MVNO  with bit rate requirements {}".format(x,c,m))
                        flag=True
                        for p in range(x):
                            B_status[n1[p]]=1
                            #print(B1,B_status)
                        break
                if flag==True:
                 break
                else:
                    #choose mcs level such that MVNO's request is met
                    v=0
                    q=[]
                    flag1=False
                    for i,g in enumerate(reversed(sorted(B1))):
                        t1 = [i for i, x1 in enumerate(B1) if x1 == g]
                        n2 = [x1 for x1 in t1 if B_status[x1] == 0]
                        if g<=c and len(n2)!=0:
                            q.append(g)
                            v=min(q)*len(q)
                            B_status[n2[0]]=1
                        if v>=m:
                            flag1=True
                            print("{} RBs with mcs {} = {} allocated for MVNO  with bit rate requirements {}".format(len(q),min(q),q,m))
                            break
                    if flag1==True:
                        break

            else:
                print("No Rbs found for MCS "+str(c)+" for MVNO with bit rate "+str(m))


