import numpy as np


def calculate(B, M):
    '''
    Method to calculate the Number of RBs required to achieve the required data rate using RSEP algorithm
    :param B: numpy list :: Single list containing all the BS's RB's channel conditions
    :param M: numpy list :: List containing data rate requirement for each MVNO
    :return: int,int :: number of allocated RBs and number of unserved MVNOs
    '''
    print("RB allocation through random RSEP algorithm")
    count = 0
    M.sort(reverse=True)
    B_status = np.zeros(len(B))
    B_status = B_status.tolist()
    m_marked = np.zeros(len(M), dtype='int32')
    m_marked = m_marked.tolist()
    for k,m in enumerate(M):
        for c in reversed(range(29)):
            if c in B:
                n = [i for i, x in enumerate(B) if x == c]
                n_zero = [x for x in n if B_status[x] == 0]
                if c >= m and (B_status[n[0]] == 0):
                    B_status[n[0]] = 1
                    print("1 RB with mcs " + str(c) + " allocated for MVNO with bit rate req ", m)
                    count+=1
                    m_marked[k] = 1
                    break
                elif len(n_zero) > 1:
                    flag = False
                    for x in range(len(n_zero)):
                        if x * c >= m:
                            print("Same: {} RBs with mcs {} allocated for MVNO  with bit rate requirements {}".format(x,c,m))
                            count+=x
                            flag = True
                            m_marked[k] = 1
                            for p in range(x):
                                B_status[n_zero[p]] = 1
                            break
                    if flag:
                        break
                    else:
                        # choose mcs level such that MVNO's request is met
                        data_rate= 0
                        mixed_mcs = []
                        flag1 = False
                        for i, g in enumerate(reversed(sorted(B))):
                            t1 = [i for i, x1 in enumerate(B) if x1 == g]
                            n_1 = [x1 for x1 in t1 if B_status[x1] == 0]
                            if g <= c and len(n_1) != 0:
                                mixed_mcs.append(g)
                                data_rate = min(mixed_mcs) * len(mixed_mcs)
                                B_status[n_1[0]] = 1
                            if data_rate >= m:
                                count += len(mixed_mcs)
                                m_marked[k] = 1
                                flag1 = True
                                print("{} RBs with mcs {} = {} allocated for MVNO  with bit rate requirements {}".format(len(mixed_mcs), min(mixed_mcs), mixed_mcs, m))
                                break
                        if flag1 == True:
                            break
                else:
                    print("No Rbs found for MCS " + str(c) + " for MVNO with bit rate " + str(m))


    return count,m_marked.count(0)