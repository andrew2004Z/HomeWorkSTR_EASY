def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return b


def ft_cmp_str(str1, str2, num):
    v = ''
    for i in range(num - 1):
        v += str1[i]
    v += str2
    for i in range(num - 1, ft_len(str1)):
        v += str1[i]
    return v
