
def quick_sort_1(ls):
    return util_quick_sort_1(ls, 0, len(ls)-1)

def util_quick_sort_1(ls, low, hi):
    if len(ls) == 1:
        return ls
    else:
        if low < hi:
            p = partition_1(ls, low, hi)
            util_quick_sort_1(ls, low, p-1)
            util_quick_sort_1(ls, p+1, hi)

# ! A, B, C
def get_pivot(ls, low, hi):
    mid = (low + hi) // 2
    pivot = mid
    if ls[mid] >= ls[low]:
        if ls[mid] > ls[hi]:
            if ls[low] <  ls[hi]:
                pivot = hi
            elif ls[low] > ls[hi]:
                pivot = low
    else:
        if ls[mid] < ls[hi]:
            if ls[low] < ls[hi]:
                pivot = low
            elif ls[low] > ls[hi]:
                pivot = hi

    # pivot = hi
    # if ls[low] < ls[mid]:
    #     if ls[mid] < ls[hi]:
    #         pivot = mid

    # elif ls[low] < ls[hi]:
    #     pivot = low
    return pivot
    # s = sorted([ls[low], ls[mid], ls[hi]])
    # if s[1] == ls[low]:
    #     return low
    # elif s[1] == ls[mid]:
    #     return mid
    # return hi
    

def partition_1(ls, low, hi):
    pivotIndex = get_pivot(ls, low, hi)
    # pivotValue = ls[pivotIndex]
    ls[pivotIndex], ls[low] = ls[low], ls[pivotIndex]

    border = low

    for i in range(low, hi+1):
        if ls[i] < ls[low]:
            border += 1
            ls[border], ls[i] = ls[i], ls[border]
            
    ls[low], ls[border] = ls[border], ls[low]
    return border

    
my_list = [4,6,5,4,3,8,9,7,1,0]


print(my_list)
quick_sort_1(my_list)
print(my_list)




