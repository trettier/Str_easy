def ft_even_place(a):
    n = True
    final = ""
    for i in a:
        if n:
            final += i
        n = not n
    return final
