# binary search
def binary(lst, key):
    low = 0
    high = len(lst) - 1
    while(low < high):
        mid = low + high // 2
        if lst[mid] == key:
            return True
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


lst = [1, 7, 3, 5, 8, 4, 3, 5, 8]
if binary(lst, 7):
    print('found')
else:
    print('not found')
