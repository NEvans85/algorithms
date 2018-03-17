"""
Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.

Example

For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
wordBoggle(board, words) = ["CODE", "RULES"].

Example

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char board

A two-dimensional array of uppercase English characters representing a rectangular Boggle board.

Guaranteed constraints:
2 ≤ board.length ≤ 4,
2 ≤ board[i].length ≤ 4,
'A' ≤ board[i][j] ≤ 'Z'.

[input] array.string words

An array of unique English words composed only of uppercase English characters.

Guaranteed constraints:
0 ≤ words.length ≤ 100,
2 ≤ words[i].length ≤ 16,
'A' ≤ words[i][j] ≤ 'Z'.

[output] array.string

Words from words that can be found on the Boggle board without duplicates and sorted lexicographically in ascending order.
"""

from collections import defaultdict

def wordBoggle(board, words):

    # Start by building a dictionary with positions of each letter present on the board
    charPosDict = defaultdict(list)
    for rIdx, row in enumerate(board):
        for cIdx, ch in enumerate(row):
            charPosDict[ch].append([rIdx, cIdx])
    present = []

    # this function returns all valid neighboring positions for a position
    def neighbors(pos):
        r, c = pos
        n = []
        for rDiff in [-1,0,1]:
            for cDiff in [-1,0,1]:
                if rDiff != 0 or cDiff != 0:
                    newR = r + rDiff
                    newC = c + cDiff
                    if 0 <= newR < len(board) and 0<= newC < len(board[newR]):
                        n.append([newR, newC])
        return n

    # This function tests if a given word can be reached from a given path.
    # Each time the next letter is found, the function is called again with the remaining
    # portion of the word and the path containing the position of that letter.
    # When a path is determined to not be valid, stacks resolve until a stack with reamining
    # positions is reached to test all possible paths.
    def wordPresent(word, path):
        if len(path) > 0:
            n = neighbors(path[-1])
            for pos in charPosDict[word[0]]:
                if pos in n and pos not in path:
                    if len(word) == 1:
                        return True
                    elif wordPresent(word[1:], path + [pos]):
                        return True
            return False
        else:
            # Since words are guaranteed to be at least 2 characters, there is no need to test
            # for word length 1 here.
            for pos in charPosDict[word[0]]:
                if wordPresent(word[1:], [pos]):
                    return True
            return False

    for word in words:
        if wordPresent(word, []):
            present.append(word)
    return sorted(present)
