def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_equal_reverse(stsr):
    a = ''
    for i in range(ft_len(stsr), 0):
        a = a + stsr[i]
    a = a.lower()
    stsr = stsr.lower()
    return a == stsr