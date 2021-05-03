def bs_iter(ls, x):
    left = 0
    right = len(ls) - 1
    mid = 0

    while left < right:
        mid = (left + right) // 2
        if x > ls[mid]:
            left = mid + 1
        elif x < ls[mid]:
            right = mid - 1
        else:
            return mid
    return -1

def bs_recur(ls, left, right, x):
    mid = (left + right) // 2
    if left < right:
        if x > ls[mid]:
            return bs_recur(ls, mid+1, right, x)
        elif x < ls[mid]:
            return bs_recur(ls, left, mid-1, x)
        else:
            return mid
    else:
        return -1
            

my_list = [1,3,5,7,9,11,13,15]
print(bs_iter(my_list, 11))
print(bs_recur(my_list, 0, len(my_list)-1, 11))