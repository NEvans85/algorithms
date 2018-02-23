"""
Before delivery, all orders at Jet are packed into boxes to protect them from damage.

Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. The package should fit inside the box, keeping in mind that the size of the package should not exceed the size of the box in any dimension (note that the package can be rotated to fit and it can be positioned upside down). For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.

Given a package pkg and available boxes, find the 0-based index of the smallest-by-volume box such that the package fits inside it, or return -1 if there is no such box.

Example

For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be
packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60) is greater than the volume of the second (5 * 5 * 2 = 50).

For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be
packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, but the first box is chosen because it has less volume overall.

For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be
packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer pkg

Array of three positive integers denoting the size of the package as its width, height and length.

Guaranteed constraints:
1 ≤ pkg[i] ≤ 500.

[input] array.array.integer boxes

Every box is given as an array of three positive integers denoting its width, height and length.
It is guaranteed that each box has a unique volume.

Guaranteed constraints:
0 ≤ boxes.length ≤ 15,
1 ≤ boxes[i][j] ≤ 500.

[output] integer

The 0-based index of the smallest-by-volume box such that the package fits inside it, or -1 if there is no such box.
"""

def packageBoxing(pkg, boxes):
    sortedPDims = sorted(pkg)
    fits = [box for box in boxes if all([sortedPDims[idx] <= bDim for idx, bDim in enumerate(sorted(box))])]
    if len(fits) == 0:
        return -1
    elif len(fits) == 1:
        return boxes.index(fits[0])
    else:
        minVolume = fits[0][0] * fits[0][1] * fits[0][2]
        minVIdx = 0
        for i in range(1, len(fits)):
            volume = fits[i][0] * fits[i][1] * fits[i][2]
            if volume < minVolume:
                minVolume = volume
                minVIdx = i
        return boxes.index(fits[minVIdx])
