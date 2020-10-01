def ft_straight_code(a):
    if a < 0:
        a = -1 * a
        t = True
    else:
        t = False
    n = 0
    i = 1
    while a > 0:
        b = a % 2
        a //= 2
        n += b * i
        i *= 10
    if t:
        n += 10 ** 6
    return n


def ft_reverse_code(a):
    if a < 0:
        a = -1 * a
        t = True
    else:
        t = False
    a = ft_straight_code(a)
    b = 0
    i = 10
    a1 = 0
    while b != 7:
        if (a // (i ** b)) % 10 == 0:
            a1 += 10 ** b
        b += 1
    if t:
        a1 += 10 ** 7
    return a1


def ft_additional_code(a):
    if a < 0:
        return ft_reverse_code(a + 1)
    if a > 0:
        return ft_reverse_code(a - 1)
    return 0