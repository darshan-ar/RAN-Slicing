import numpy as np


def calculate(B, M):
    '''
    Method to calculate the Number of RBs required to achieve the required data rate using lowest available MCS level
    :param B: numpy list :: Single list containing all the BS's RB's channel conditions
    :param M: numpy list :: List containing data rate requirement for each MVNO
    :return: int,int :: number of allocated RBs and number of unserved MVNOs
    '''
    print("RB allocation through lowest MCS selection")
    count = 0
    B_status = np.zeros(len(B),dtype='int32')
    M.sort(reverse=True)
    lowest_mcs_level = min(B)
    B_status = B_status.tolist()
    m_marked=np.zeros(len(M),dtype='int32')
    m_marked=m_marked.tolist()

    for k,m in enumerate(M):
        if lowest_mcs_level * len(B) <= m:
            print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))
        else:
            flag = False
            for n in range(len(B)):
                if n * lowest_mcs_level >= m and n <= B_status.count(0):
                    print("{} RB's with mcs {} was used to achieve data rate of {}".format(n, lowest_mcs_level, m))
                    count += n
                    m_marked[k]=1
                    for p in range(n):
                        B_status[p] = 1
                        flag = True
                    break
            if not flag:
                print("MVNO data rate of {} cannot be achieved with this mcs selection policy".format(m))

    return count,m_marked.count(0)
