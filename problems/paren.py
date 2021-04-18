mapping = {')': '(', ']': '[', '}': '{'}

def paren_check(s: str) -> bool:
    stack = []
    
    for char in s:
        if char not in mapping:
            stack.append(char)

        else:
            current_ch = stack.pop() if stack else '#'
            if current_ch != mapping[char]:
                return False

    return not stack

test_1 = '([]{()})'
test_2 = '[(}){}]'

print(paren_check(test_1))
print(paren_check(test_2))