def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_three_str(str1, str2, str3):
    result = ""
    for i in range(ft_len(str1)):
        flag = 0
        for j in range(ft_len(str2)):
            if str1[i + j] != str2[j]:
                flag = 1
        if flag == 0:
            for k in range(i):
                result = result + str1[k]

            result = result + str3

            for k in range(ft_len(str2) + i, ft_len(str1)):
                result = result + str1[k]
            return result
    return -1
