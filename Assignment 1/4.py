#pattern
#working on it
import math
n = int(input())
rows = math.ceil(n / 4)
mid = math.ceil(rows / 4) + 1
temp=mid+1
star = 2
start = n - mid
temp1=start
begin = 1
for i in range(0, rows):
    print('\n')
    cols = (temp * 2)
    temp -= 1
    if i != 0:
      for k in range(star + 1):
            print('*', end='')
            star += 2
    for j in range(0, cols):
        if j<temp+1:
            print(begin, end='0')
            begin += 1
        else:
            if start<n:
                print(start, end='0')
                start += 1
            else:
                print(start, end='')
    temp1 -= 2
    start=temp1

            





       

        


