import lowest_mcs,highest_mcs,average_mcs,random_mcs,rsep
import numpy as np
import matplotlib.pyplot as plt
B = int(input("Enter the number of Base Stations: "))
M = int(input("Enter the number of MVNO's: "))

D=[]
Bs=[]
Bs1=np.zeros((4,4),dtype='int32')
for i in range(M):
    D.append(int(input("Enter the Data Rate Requirement for MVNO "+str(i+1)+": ")))

print("{} Base stations, each having 16 RBs with channel conditions:".format(B))
for i in range(B):
    Bs.append(np.random.randint(1,30,(4,4)))
    print("B"+str(i+1)+": "+str(Bs[i]))
    Bs1=np.concatenate((Bs1,Bs[i]),axis=1)
B=Bs1.tolist()
B = sum(B,[])
print(B)
Bsort=sorted(B)
print(Bsort)
B = Bsort[16:]
print(B)
print("Now Benchmarking our algorithm with static allocation methods for 1 TTI")

p=[]
print("******************************************************************************************************************************************")
p.append(lowest_mcs.calculate(B,D))
print("******************************************************************************************************************************************")
p.append(highest_mcs.calculate(B,D))
print("******************************************************************************************************************************************")
p.append(average_mcs.calculate(B,D))
print("******************************************************************************************************************************************")
p.append(random_mcs.calculate(B,D))
print("******************************************************************************************************************************************")
p.append(rsep.calculate(B,D))

#Plot details
q=['Lowest MCS selection','Highest MCS selection','Average MCS selection','Random MCS selection','RSEP algorithm']
w=0.3
r = np.arange(len(p))

z=plt.bar(r,p, color='red', width=w, edgecolor='red', label='Number of RBs utilized in each methods')
plt.xlabel('Different RB allocation Algorithms', fontsize="30", fontweight='bold')
plt.ylabel('Number of RBs', fontsize="30", fontweight='bold')
plt.xticks([r for r in range(len(p))], q)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%0.2f' %height,ha='center', va='bottom',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
autolabel(z)
plt.legend(fontsize=20)
plt.show()
