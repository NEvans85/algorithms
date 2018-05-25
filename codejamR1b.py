class MinHeap:
    def __init__(self):
        self.store = [0]
        self.currentSize = 0

    def size(self):
        return self.currentSize

    def insert(self, value, idx):
        self.store.append((value,idx))
        self.currentSize += 1
        self.percUp(self.currentSize)

    def peekRoot(self):
        return self.store[1]

    def deleteRoot(self):
        rootVal = self.store[1]
        self.store[1] = self.store[self.currentSize]
        self.store.pop()
        self.currentSize -= 1
        self.percDown(1)
        return rootVal

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx][0] < self.store[idx // 2][0]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2

    def percDown(self, idx):
        while idx * 2 <= self.currentSize:
            sc = self.smallestChild(idx)
            if self.store[idx][0] > self.store[sc][0]:
                temp = self.store[sc]
                self.store[sc] = self.store[idx]
                self.store[idx] = temp
            idx = sc

    def smallestChild(self, idx):
        if idx * 2 + 1 > self.currentSize or self.store[idx * 2][0] < self.store[idx * 2 + 1][0]:
            return idx * 2
        else:
            return idx * 2 + 1

t = int(input())
for case in range(t):
    n, l = map(int, input.split())
    if 100 % n == 0:
        print("Case #{}: 100".format(case + 1))
    else:
        percentPerPerson = 100.0 / n
        minForRoundUp = 1
        while (minForRoundUp * percentPerPerson) % 1 < 0.5:
            minForRoundUp += 1
        c = map(int, input.split())
        responders = sum(c)
        toRespond = n - responders

        def responsesNeeded(num):
            if (num * percentPerPerson) % 1 >= 0.5:
                return 10 ** 5
            else:
                curr = num + 1
                while (curr * percentPerPerson) % 1 < 0.5:
                    curr += 1
                return curr - num

        responseHeap = MinHeap()
        for idx, val in enumerate(c):
            responseHeap.insert(responsesNeeded(val), idx)
        while toRespond > 0:
            bestChoice = responseHeap.deleteRoot()
            if bestChoice[0] > minForRoundUp * 2 and minForRoundUp * 2 <= toRespond:
                c.append(minForRoundUp)
                c.append(minForRoundUp)
                toRespond -= 2 * minForRoundUp
            elif bestChoice[0] <= toRespond:
                c[bestChoice[1]] += bestChoice[0]
                toRespond -= bestChoice[0]
            elif minForRoundUp <= toRespond:
                c.append(minForRoundUp)
                toRespond -= toRespond
        totalPercentage = sum([round(percentPerPerson * r) for r in c])
        print("Case #{}: {}".format(case + 1, totalPercentage))
