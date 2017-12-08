# prompt: https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem

# Although the logic is sound, this implementation is wildly inefficient.
def inputToIntList(s):
    return [int(el) for el in s.split(" ")]

def combinations(nums):
    results = []
    for i in range(len(nums) - 1):
        j = i + 1
        while j < len(nums):
            results.append([nums[i], nums[j]])
            j += 1
    return results

def distance(connDict, a, b):
    visited = [a]
    pathStack = [[conn] for conn in connDict[a]]
    while len(pathStack) > 0:
        path = pathStack.pop()
        if path[-1] == b:
            return len(path)
        else:
            visited.append(path[-1])
            for nextConn in connDict[path[-1]]:
                if nextConn not in visited:
                    pathStack.append(path + [nextConn])

connDict = {}
n, q = inputToIntList(input())
for _ in range(n - 1):
    a, b = inputToIntList(input())
    if a in connDict:
        connDict[a].append(b)
    else:
        connDict[a] = [b]
    if b in connDict:
        connDict[b].append(a)
    else:
        connDict[b] = [a]
for _ in range(q):
    l = int(input())
    nums = inputToIntList(input())
    pairs = combinations(nums)
    valueList = [0]
    for pair in pairs:
        valueList.append(pair[0] * pair[1] * distance(connDict, pair[0], pair[1]))
    print (sum(valueList))
