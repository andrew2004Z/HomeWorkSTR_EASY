def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l

def ft_find_str(str1, str2):
    for i in range(ft_len(str1)):
        flag = 0
        for j in range(ft_len(str2)):
            if str1[i+j] != str2[j]:
                flag = 1
        if flag == 0:
            return i
    return -1