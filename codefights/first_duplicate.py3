# https://codefights.com/interview-practice/task/pMvymcahZ8dY4g75q

def firstDuplicate(a):
    seen = [0] * len(a)
    for el in a:
        if seen[el - 1] == 0:
            seen[el - 1] = 1
        else:
            return el
    return -1
