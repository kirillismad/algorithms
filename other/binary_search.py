def binary_search(lst, searched):
    start_index, end_index = 0, len(lst) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        value = lst[middle_index]
        if value == searched:
            return middle_index
        if value > searched:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1


def r_binary_search(lst, searched, start_index=0, end_index=None):
    end_index = len(lst) - 1 if end_index is None else end_index

    middle_index = (start_index + end_index) // 2
    value = lst[middle_index]

    if value == searched:
        return middle_index
    if value > searched:
        return r_binary_search(lst, searched, start_index, end_index=middle_index - 1)
    return r_binary_search(lst, searched, start_index + 1, end_index)


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(lst, 4) == 3
    assert r_binary_search(lst, 4) == 3


if __name__ == '__main__':
    main()
