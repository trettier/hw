def right(a):
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


def dovod(a):
    if a < 0:
        a = -1 * a
        t = True
    else:
        t = False
    a = right(a)
    b = 0
    d = 10
    x = 7
    while x != -1:
        c = (a // (d ** x)) % 10
        x -= 1
        if c == 0:
            c += 1
        else:
            c -= 1
        b += c * (10 ** (x + 1))
    if not t:
        b -= 10 ** 7
    return b

def last(a):
    if a < 0:
        return dovod(a + 1)
    return dovod(a - 1)




print(right(10))
print(dovod(-10))
print(last(-10))