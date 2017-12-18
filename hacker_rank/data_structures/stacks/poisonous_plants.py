# prompt: https://www.hackerrank.com/challenges/poisonous-plants/problem

import sys

def poisonousPlants(p):
    decQueues = createQueues(p)
    days = 0
    while len(decQueues) > 1:
        for i in range(1, len(decQueues)):
            decQueues[i].pop(0)
        decQueues = [x for x in decQueues if x != []]
        decQueues = mergeQueues(decQueues)
        days += 1
    return days

def createQueues(p):
    queues = [[p[0]]]
    for el in p[1:]:
        if el <= queues[-1][-1]:
            queues[-1].append(el)
        else:
            queues.append([el])
    return queues

def mergeQueues(qs):
    newQueues = [qs[0]]
    for i in range(1, len(qs)):
        if qs[i][0] <= newQueues[-1][-1]:
            newQueues[-1] += qs[i]
        else:
            newQueues.append(qs[i])
    return newQueues

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = poisonousPlants(p)
    print(result)
