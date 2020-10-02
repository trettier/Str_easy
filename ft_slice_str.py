import ft_len


def ft_slice_str(a, b, c):
    n = ft_len.ft_len(a)
    d = ""
    if n > c:
        for i in range(n):
            if i + 1 > b and i + 1 < c:
                d += a[i]
    else:
        for i in range(n):
            if i + 1 > b:
                d += a[i]
    return d
