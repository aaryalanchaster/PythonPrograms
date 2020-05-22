# spliting odd and even numbers

lst1 = [i for i in range(1, 21)]
lst2, lst3 = [], []
for num in lst1:
    if num % 2 == 0:
        lst2.append(num)
    else:
        lst3.append(num)

print(lst2)
print(lst3)
