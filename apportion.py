from math import sqrt
from queue import PriorityQueue

def apportion(house_size, entitlement):
    length = len(entitlement)
    apportionment = [1 for i in range(length)]

    pqueue = PriorityQueue(maxsize=length)
    for i in range(length):
        pqueue.put((-entitlement[i] / sqrt(apportionment[i] * (apportionment[i] + 1)), i))

    for i in range(house_size - length):
        j = pqueue.get()[1]
        apportionment[j] += 1
        pqueue.put((-entitlement[j] / sqrt(apportionment[j] * (apportionment[j] + 1)), j))

    return apportionment
