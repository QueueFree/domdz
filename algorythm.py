array = [18, 7, 9, 100, 3, -2, 6, 5, 1]

val = 9
def sel_sort(i):
    ar = []
    while len(i) > 0:
        ar.append(min(i))
        i.remove(min(i))

    return ar

print(f'не сортированый список: {array}')
print(f'сортированый список: {sel_sort(array)}')

def binary_poisk(lst, find):
    first = 0
    last = len(lst) - 1
    find_res = False

    while first <= last and not find_res:
        middle = (first + last) // 2
        mid = lst[middle]
        if mid == find:
            find_res = True
            return find_res
        if mid > find:
            last = middle - 1
        else:
            first = middle + 1
    return find_res


end = binary_poisk([34, 67, 98, 100, 35], 67)
if end:
    print(f'число было найдено')
else:
    print('число не было найдено')
