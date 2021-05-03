


# def bubble(ls):
#     last_index = len(ls) - 1
#     is_sorted = False

#     while not is_sorted:
#         is_sorted = True
#         for i in range(0, last_index):
#             if ls[i] > ls[i+1]:
#                 is_sorted = False
#                 ls[i], ls[i+1] = ls[i+1], ls[i]
#         last_index -= 1

#     return ls

# def bubble_2(ls):
#     for i in range(len(ls)-1, 0, -1):
#         for j in range (i):
#             if ls[j] > ls[j+1]:
#                 ls[j], ls[j+1] = ls[j+1], ls[j]
#     return ls


# print(bubble(my_list))
# print(bubble_2(my_list))

# def selection_sort(ls):
#     for i in range(0, len(ls)-1):
#         minValue = i
#         for j in range(i+1, len(ls)):
#             if ls[minValue] > ls[j]:
#                 minValue = ls[j]

#         if minValue != i:
#             ls[i], ls[minValue] = ls[minValue], ls[i]
#     return ls

# print(selection_sort(my_list))

def merge_sort(ls):
    util_merge_sort(ls, 0, len(ls) - 1)

def util_merge_sort(ls, first, last):
    if first < last:
        mid = (first + last) // 2
        util_merge_sort(ls, first, mid)
        util_merge_sort(ls, mid+1, last)
        merge(ls, first, mid, last)

def merge(ls, l, m, r):
    len_l = m - l + 1
    len_r = r - m

    ls_l = ls[l:m+1]
    ls_r = ls[m+1:r+1]
    print(ls_l, ls_r, sep='\t')

    i = j = 0
    k = l
    
    while i < len_l and j < len_r:
        if ls_l[i] <= ls_r[j]:
            ls[k] = ls_l[i]
            i += 1
        else:
            ls[k] = ls_r[j]
            j += 1
        k += 1
    
    while i < len_l:
        ls[k] = ls_l[i]
        i += 1
        k += 1

    while j < len_r:
        ls[k] = ls_r[j]
        j += 1
        k += 1


def simple_quick_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        pivot = ls.pop()
        
        items_greater = []
        items_lower = []

        for item in ls:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        
        return simple_quick_sort(items_lower) + [pivot] + simple_quick_sort(items_greater)

def insertion_sort(ls):
    for i in range(1, len(ls)):
        while ls[i] < ls[i-1] and i > 0:
            ls[i], ls[i-1] = ls[i-1], ls[i]
            i -= 1
    return ls

# [2,4,3,1,5,6]
my_list = [4,6,5,4,3,8,9,7,1,0]

# merge_sort(my_list)
# print(my_list)

# print(simple_quick_sort(my_list))

print(insertion_sort(my_list))