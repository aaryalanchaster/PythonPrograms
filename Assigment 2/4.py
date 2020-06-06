def div(a, b):
    try:
        print(a / b)
    except:
        print('/ by 0')


n1, n2 = map(int, input().split())
div(n1, n2)


fname = input()
try:
    f = open(fname).read()
    for lines in f:
        print(lines, end="")
except FileNotFoundError:
    print('file not found')
