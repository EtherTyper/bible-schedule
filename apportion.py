from math import sqrt

def apportion(value, weights):
    length = len(weights)
    apportionment = [1 for i in range(len(weights))]

    for i in range(value - length):
        index = max(range(length),
            key=lambda j: weights[j] / sqrt(apportionment[j] * (apportionment[j] + 1)))
        apportionment[index] += 1

    return apportionment
