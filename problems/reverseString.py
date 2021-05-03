def reverse_string_1(s):
    return ' '.join(reversed(s.split()))

def reverse_string(s):
    word = ''
    sent = []
    for i in s:
        if i != ' ':
            word += i
        else:
            sent.append(word)
            word = ''
    sent.append(word)
    print(sent)

# print(reverse_string_1('Hello World this is Sam'))
reverse_string('Hello World this is Sam')