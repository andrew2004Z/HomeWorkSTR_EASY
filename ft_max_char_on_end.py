def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_max_char_on_end(stsr):
    lst = '1234567890'
    maxx = 0
    lenn = 0
    for i in range(ft_len(stsr)):
        if stsr[i] in lst:
            lenn += 1
        elif stsr[i] not in lst:
            if lenn > maxx:
                maxx = lenn
            lenn = 0
    return maxx