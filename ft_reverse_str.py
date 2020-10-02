import ft_len


def ft_reverse_str(a):
    b = ""
    for i in range(ft_len.ft_len(a), 0, -1):
        b += a[i - 1]
    return b
