str = input()
#print(len(str.split()) - 1)
#print(str.count(' '))
print(len(str)-sum(map(len,str.split(' '))))