def reverse_string_1(s):
    return ' '.join(reversed(s.split()))

def reverse_string(s):
    length = len(s)

    words = list()
    spaces = [' ']
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and i not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    # print(f'show me i = {i} and coutner = {counter}')
    return words
    # while len(words) > 0:
    #     temp = words.pop(-1)
    #     print(temp)
    #     result = result + ' ' + temp
    # return result


# print(reverse_string_1('Hello World this is Sam'))
# print(reverse_string('Hello World this is Sam'))
# st = []
# lst = 'abcdefghi'
# st.append(lst[0:2])
# st.append(lst[2:4])
# print(st)

# def rev(s):
#     return s.split()[::-1]

# print(rev('Hello World this is Sam'))


ls = [1,1,2]
s = set()
for i in ls:
    s.add(i)
print(len(s))
