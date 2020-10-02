def ft_cmp_str(a, b, c):
    n = 0
    for i in a:
        n += 1
    d = ""
    for i in range(n):
        if i + 1 != c:
            d += a[i]
        else:
            d += b + a[i]
    return d
