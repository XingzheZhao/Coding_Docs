my_sorted_list = [0, 1, 2, 3, 4, 5, 6, 10, 14, 20, 30, 35, 40, 45, 46, 60, 66, 70, 89, 90]
temp = [1,2,3,4]

def iter_binary_search(ls, item):
    first = 0
    last = len(ls) - 1
    mid = 0

    while first <= last:
        mid = (first + last) // 2
        if item > ls[mid]:
            first = mid + 1
        elif item < ls[mid]:
            last = mid - 1
        else:
            return mid
    return -1


print(iter_binary_search(my_sorted_list, 6))
print(iter_binary_search(temp, 1))

def recur_binary_search(ls, left, right, target):
    
    if left < right:
        mid = (left + right) // 2

        if (target < ls[mid]):
            return recur_binary_search(ls, left, mid-1, target)
        elif (target > ls[mid]):
            return recur_binary_search(ls, mid+1, right, target)
        else:
            return mid
    else:
        return -1

print(recur_binary_search(my_sorted_list, 0, len(my_sorted_list)-1,10))
print(recur_binary_search(my_sorted_list, 0, len(my_sorted_list)-1,122))
print(recur_binary_search(my_sorted_list, 0, len(my_sorted_list)-1,60))
