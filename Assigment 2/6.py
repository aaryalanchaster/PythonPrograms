# anagram
from itertools import count

import numpy as np

NO_OF_CHARS = 256


def anagram(s1, s2):
    count = [0] * NO_OF_CHARS
    for c1, c2 in zip(s1, s2):
        count[ord(c1)] += 1
        count[ord(c2)] -= 1
    if np.count_nonzero(count) != 0:
        print('not anagram')
        return
    print('anagram')
    return


str1 = input()
str2 = input()
anagram(str1, str2)
