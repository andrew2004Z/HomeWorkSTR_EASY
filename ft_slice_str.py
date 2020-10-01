def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_slice_str(str1, start, end):
    result = ""
    for i in range(start, end + 1):
        if i >= ft_len(str1):
            break
        result = result + str1[i]
    return result