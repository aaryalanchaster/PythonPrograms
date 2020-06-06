# given the string sort it in descending order based on frequency of characters
from collections import Counter
a = input()
b = Counter(a).most_common()
print("".join([i[0]*i[1] for i in b]))
