def ft_find_str(a, b):
    n = 0
    for i in a:
        n += 1
    n1 = 0
    for i in b:
        n1 += 1
    c = -1
    d = ""
    t = True
    for i in range(n):
        d += a[i]
        if b in d and t:
            t = False
            c = i - n1 + 2
    return c
