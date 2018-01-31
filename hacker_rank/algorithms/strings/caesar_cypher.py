

import sys

def caesarCipher(s, k):
    result = ''
    for ch in s:
        if ch.isupper():
            chOrd = ord(ch) + k
            while chOrd > 90:
                chOrd -= 26
            result += chr(chOrd)
        elif ch.islower():
            chOrd = ord(ch) + k
            while chOrd > 122:
                chOrd -= 26
            result += chr(chOrd)
        else:
            result += ch
    return result

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
