import glob


if __name__ == '__main__':
    # list of all folders
    lst = glob.glob('/home/kaibo/DATA/*/*/')
    # divide into groups of 50
    n_groups = len(lst) // 50 + 1
    for group_num in range(n_groups):
        if group_num == n_groups - 1:
            sub_lst = lst[group_num * 50:]
        else:
            sub_lst = lst[group_num * 50: (group_num + 1) * 50]
        # create txt file specifying subjects in each group
        with open(f'./group/group_{group_num}.txt', 'w') as f:
            for sub in sub_lst:
                curr_sub = '/'.join(sub.split('/')[-2:])
                f.write(curr_sub + '\n')
