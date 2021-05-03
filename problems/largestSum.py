def largest(arr):
    if len(arr) < 1:
        return
    current_max = overall_max = arr[0]

    for i in arr[1:]:
        current_max = max(current_max + i, i)
        overall_max = max(current_max, overall_max)
    
    return overall_max

def largest2(arr):
    if len(arr) < 1:
        return
    current_max = max_sum = arr[0]

    for i in arr[1:]:
        if current_max + i <= i:
            current_max = i
        else:
            current_max = current_max + i
        if current_max > max_sum:
            max_sum = current_max

    return max_sum


ls = [-20,1,2,-9,5,3,-4,5,2,-4,1,8,4,-4,-6,-2,9,12,3,4]
result = largest(ls)
result2 = largest2(ls)
print(result)
print(result2)