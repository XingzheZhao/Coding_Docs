
def pairSum(ar, num):
    if len(ar) < 2:
        print('Not enough elements')
        return
    
    seen = set()
    output = set()

    for i in ar:
        target = num - i
        if target not in seen:
            seen.add(i)
        else:
            output.add((i, target))
    print('\n'.join(map(str, output)))

lst = [1,3,1,2,2,2,4,3,5]
numb = 4
pairSum(lst, numb)