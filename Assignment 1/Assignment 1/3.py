# finding prime

number = int(input())
for num in range(1, number + 1):
    count = 0
    for i in range(2, num // 2):
        if (num % i == 0):
            count += 1
            break
    if (count == 0 and num != 1):
        print(num)
