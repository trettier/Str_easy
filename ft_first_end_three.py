import ft_len


def ft_first_end_three(a):
    b = ft_len.ft_len(a)
    c = ""
    d = ""
    if b > 5:
        for i in range(3):
            c += a[i]
            d += a[-(3 - i)]
        print(c, f"\n{d}")
    else:
        for i in a:
            print(a[0])
