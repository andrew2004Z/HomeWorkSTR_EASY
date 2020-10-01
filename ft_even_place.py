def ft_len(str):
    c = 0
    for i in str:
        c += 1
    return c


def ft_even_place(stsr):
    r = ""
    l = ft_len(stsr)
    for i in range(l):
        if i % 2 == 0:
            r = r + stsr[i]
    return r
