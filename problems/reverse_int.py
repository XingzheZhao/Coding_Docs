def reverse(x: int) -> int:
    if x > - x**31 and x < x**31 - 1:
        result = 0
        negative = False

        if x < 0:
            negative = True
            x = -1 * x

        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
        return result
    else:
        return 0

print(reverse(654123))