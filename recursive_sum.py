def sum_of_list(x):
    if len(x) > 0:
        return x[0] + sum_of_list(x[1:])
    else:
        return 0


if __name__ == '__main__':
    print(sum_of_list([1, 2, 3, 4, 5]))
