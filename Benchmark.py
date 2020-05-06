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

Bsort=sorted(B)

B = Bsort[16:]

print("Now Benchmarking our algorithm with static allocation methods for 1 TTI")

p=[]
q=[]
print("******************************************************************************************************************************************")
a,s1=lowest_mcs.calculate(B,D)
print("******************************************************************************************************************************************")
b,s2=highest_mcs.calculate(B,D)
print("******************************************************************************************************************************************")
c,s3=average_mcs.calculate(B,D)
print("******************************************************************************************************************************************")
d,s4=random_mcs.calculate(B,D)
print("******************************************************************************************************************************************")
e,s5=rsep.calculate(B,D)
print("******************************************************************************************************************************************")

if a==0 or s1 !=0:
    print("Lowest MCS level selection yields no result")
else:
    p.append(a)
    q.append('Lowest MCS selection')
if b==0 or s2!=0:
    print("Highest MCS level selection yields no result")
else:
    p.append(b)
    q.append('Highest MCS selection')
if c==0 or s3!=0:
    print("Average MCS level selection yields no result")
else:
    p.append(c)
    q.append('Average MCS selection')
if d==0 or s4!=0:
    print("Random MCS level selection yields no result")
else:
    p.append(d)
    q.append('Random MCS selection')
if e==0 or s5!=0:
    print("RSEP MCS level selection yields no result")
else:
    p.append(e)
    q.append('RSEP MCS selection')

#Plot details
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
