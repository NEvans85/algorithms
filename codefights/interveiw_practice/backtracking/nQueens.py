"""
In chess, queens can move any number of squares vertically, horizontally, or diagonally. The n-queens puzzle is the problem of placing n queens on an n × n chessboard so that no two queens can attack each other.

Given an integer n, print all possible distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the placement of the n queens, where the solutions are arrays that contain permutations of [1, 2, 3, .. n]. The number in the ith position of the results array indicates that the ith column queen is placed in the row with that number. In your solution, the board configurations should be returned in lexicographical order.

Example

For n = 1, the output should be
nQueens(n) = [[1]].

For n = 4, the output should be

  nQueens(n) = [[2, 4, 1, 3],
                [3, 1, 4, 2]]
This diagram of the second permutation, [3, 1, 4, 2], will help you visualize its configuration:



The element in the 1st position of the array, 3, indicates that the queen for column 1 is placed in row 3. Since the element in the 2nd position of the array is 1, the queen for column 2 is placed in row 1. The element in the 3rd position of the array is 4, meaning that the queen for column 3 is placed in row 4, and the element in the 4th position of the array is 2, meaning that the queen for column 4 is placed in row 2.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

The size of the board.

Guaranteed constraints:

1 ≤ n ≤ 10.

[output] array.array.integer

All possible distinct board configurations of the placement of the n queens, ordered lexicographically.
"""

def nQueens(n):
    placements = []
    workingPlacement = []

    # this function tests whether a placement is valid
    def canPlace(rIdx, cIdx):
        for pcIdx, prIdx in enumerate(workingPlacement):
            if rIdx == prIdx or abs(cIdx - pcIdx) == abs(rIdx - prIdx):
                return False
        return True

    # This recursive function tests each row for validity, testing the next column if a
    # placement is valid. When a column contains no valid rows, the previous stack resumes,
    # testing the next valid row for it's column. When the workingPlacement list is the right
    # length (n), it is complete and the solution is added to a list to be returned.
    def testPlacements(cIdx):
        for rIdx in range(n):
            if canPlace(rIdx, cIdx):
                workingPlacement.append(rIdx)
                if len(workingPlacement) == n:
                    placements.append([el + 1 for el in workingPlacement])
                else:
                    testPlacements(cIdx + 1)
                workingPlacement.pop()

    testPlacements(0)
    return placements
