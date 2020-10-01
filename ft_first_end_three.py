def ft_first_end_three(stsr):
    if ft_len(stsr) > 5:
        print(stsr[:3] + stsr[-3:])
    else:
        print(stsr[0] * ft_len(stsr))