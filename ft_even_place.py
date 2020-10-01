def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_even_place(a):
    c = str()
    for i in range(ft_len(a)):
        if i % 2 == 1:
            c += a[i]
    return c
