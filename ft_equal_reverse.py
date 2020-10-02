import ft_len


def ft_equal_reverse(a):
    n = ft_len.ft_len(a)
    for i in range(n // 2):
        if a[i] != a[-(i + 1)]:
            return "false"
    return "true"
