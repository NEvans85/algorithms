# prompt: https://www.hackerrank.com/challenges/crossword-puzzle/problem

"""
This algorithm starts by finding the first blank space and determining the
direction, length, and starting pos of the word from it. It then tries
each word with that length in the space. If the word fits, the partially
completed board and the hint list without the word are passed back into
the crosswordPuzzle method which repeats the aforementioned process.
Once the hints list is empty, the puzzle is solved. If one of the
recursive calls results in a word not fitting into the puzzle, the
algorithm bubbles up to the last blank which could have been another
word, then it tries that next word. This implementation assumes a solution
exists for the puzzle.
"""

import sys

def crosswordPuzzle(board, hints):
    if len(hints) == 0:
        return board
    hintsByLen = sortHints(hints)
    nextBlank = findNextBlank(board)
    direction = findDir(board, nextBlank)
    wordStart = findStart(board, nextBlank, direction)
    wordLen = findLen(board, wordStart, direction)
    for hint in hintsByLen[wordLen]:
        boardCopy = [row[:] for row in board]
        hintsCopy = hints[:]
        currPos = wordStart[:]
        if direction == 'h':
            for ch in hint:
                if boardCopy[currPos[0]][currPos[1]] not in [ch, '-']:
                    return False
                else:
                    boardCopy[currPos[0]][currPos[1]] = ch
                    currPos[1] += 1
        else:
            for ch in hint:
                if boardCopy[currPos[0]][currPos[1]] not in [ch, '-']:
                    return False
                else:
                    boardCopy[currPos[0]][currPos[1]] = ch
                    currPos[0] += 1
        hintsCopy.remove(hint)
        solved = crosswordPuzzle(boardCopy, hintsCopy)
        if solved:
            break
    if solved:
        return [''.join(row) for row in solved]
    else:
        return False

def displayBoard(board):
    print("\n".join([''.join(row) for row in board]))

def sortHints(hints):
    sHints = {}
    for hint in hints:
        if len(hint) in sHints:
            sHints[len(hint)].append(hint)
        else:
            sHints[len(hint)] = [hint]
    return sHints

def findNextBlank(board):
    for rIdx, row in enumerate(board):
        for cIdx, ch in enumerate(row):
            if ch == '-':
                return [rIdx, cIdx]
    return False

def findDir(board, blank):
    if blank[1] < len(board[blank[0]]) - 1 and board[blank[0]][blank[1] + 1] == '-':
        return 'h'
    else:
        return 'v'

def findStart(board, blank, direction):
    startPos = blank[:]
    if direction == 'h':
        while startPos[1] > 0 and board[startPos[0]][startPos[1] - 1] != '+':
            startPos[1] -= 1
    else:
        while startPos[0] > 0 and board[startPos[0] - 1][startPos[1]] != '+':
            startPos[0] -= 1
    return startPos

def findLen(board, start, direction):
    length = 1
    currPos = start[:]
    if direction == 'h':
        while currPos[1] < len(board[currPos[0]]) - 1 and board[currPos[0]][currPos[1] + 1] != '+':
            currPos[1] += 1
            length += 1
    else:
        while currPos[0] < len(board) - 1 and board[currPos[0] + 1][currPos[1]] != '+':
            currPos[0] += 1
            length += 1
    return length

if __name__ == "__main__":
    crossword = []
    crossword_i = 0
    for crossword_i in range(10):
       crossword_t = str(input().strip())
       crossword.append(crossword_t)
    hints = input().strip().split(';')
    crossword = [list(row) for row in crossword]
    result = crosswordPuzzle(crossword, hints)
    print ("\n".join(map(str, result)))
