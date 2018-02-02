# prompt: https://www.hackerrank.com/challenges/gem-stones/problem

"""
This algorithm finds the number of characters an array of strings have
in common. It converts them to sets then finds the intersection between
all of the sets to get a set of common characters, then returns the length
of that result set.
"""

def gemstones(arr):
    setList = [set(list(el)) for el in arr]
    resultSet = setList[0]
    for i in range(1,len(setList)):
        resultSet = resultSet & setList[i]
    return len(resultSet)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
