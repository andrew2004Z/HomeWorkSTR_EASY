def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_reverse_str(stsr):
    a = ''
    for i in range(len(stsr), 0, -1):
        a = a + stsr[i]
    return a