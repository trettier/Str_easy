def ft_max_char_on_end(a):
    b = 1
    n = 0
    for i in a:
        n += 1
    c = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            b += 1
        else:
            if b > c:
                c = b
            b = 0
    print(c)
