# prompt: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

def getBiggestRegion(grid):
    def neighbors(r, c):
        diffs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        possPos = [[r + d[0], c + d[1]] for d in diffs]
        valid = [p for p in possPos if 0<=p[0]<len(grid) and 0<=p[1]<len(grid[0]) and gridCopy[p[0]][p[1]] == 1]
        return valid

    def visit(r, c):
        nPoses = neighbors(r,c)
        count = len(nPoses)
        for pos in nPoses:
            gridCopy[pos[0]][pos[1]] = -1
        for pos in nPoses:
            count += visit(*pos)
        return count

    gridCopy = [row[:] for row in grid]
    bestCount = 0
    for rIdx, row in enumerate(gridCopy):
        for cIdx, col in enumerate(row):
            if gridCopy[rIdx][cIdx] == 1:
                gridCopy[rIdx][cIdx] = -1
                regionCount = 1 + visit(rIdx, cIdx)
                if regionCount > bestCount:
                    bestCount = regionCount
    return bestCount


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
