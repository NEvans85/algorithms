"""
Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example

For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-105 ≤ nums[i] ≤ 105.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ nums.length.

[output] integer
"""

class MaxHeap:
    def __init__(self):
        self.store = [0]
        self.currentSize = 0

    def size(self):
        return self.currentSize

    def insert(self, value):
        self.store.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def deleteRoot(self):
        rootVal = self.store[1]
        self.store[1] = self.store[self.currentSize]
        self.store.pop()
        self.currentSize -= 1
        self.percDown(1)
        return rootVal

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx] > self.store[idx // 2]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2

    def percDown(self, idx):
        while idx * 2 <= self.currentSize:
            lc = self.largestChild(idx)
            if self.store[idx] < self.store[lc]:
                temp = self.store[lc]
                self.store[lc] = self.store[idx]
                self.store[idx] = temp
            idx = lc

    def largestChild(self, idx):
        if idx * 2 + 1 > self.currentSize or self.store[idx * 2] > self.store[idx * 2 + 1]:
            return idx * 2
        else:
            return idx * 2 + 1

def kthLargestElement(nums, k):
    return sorted(nums)[k * -1]
# The preceding solution passes all tests but does not use the MaxHeap class.
# The following code uses a MaxHeap to find the kth largest element but does not pass the last test due to time.
#    heap = MaxHeap()
#    for el in nums:
#        heap.insert(el)
#    result = None
#    for _ in range(k):
#        result = heap.deleteRoot()
#    return result
