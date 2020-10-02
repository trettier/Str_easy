def ft_percent_lower_uppercase(a):
    up = 0
    down = 0
    for i in a:
        if i == i.upper():
            up += 1
        elif i == i.lower():
            down += 1
    return (down / up) * 100
