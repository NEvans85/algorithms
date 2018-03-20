"""
Given a string of digits, return all of the possible non-empty letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:



The resulting array should be sorted lexicographically.

Example

For buttons = "42", the output should be
pressingButtons(buttons) = ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] string buttons

A string composed of digits ranging from '2' to '9'.

Guaranteed constraints:

0 ≤ buttons.length ≤ 7.

[output] array.string
"""

def pressingButtons(buttons):
    digitChDict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
    combos = []
    for digit in buttons:
        if len(combos) == 0:
            combos = digitChDict[digit]
        else:
            newCombos = []
            for combo in combos:
                for ch in digitChDict[digit]:
                    newCombos.append(combo + ch)
            combos = newCombos[:]
    return combos
