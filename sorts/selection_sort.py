from itertools import islice
from operator import gt, lt


def get_index(arr, op):
    result = arr[0]
    result_index = 0

    for i, value in enumerate(islice(arr, 1, len(arr)), start=1):
        if op(value, result):
            result, result_index = value, i

    return result_index


def selection_sort(arr, *, reverse=False):
    arr = arr.copy()
    op = gt if reverse else lt
    for i in range(len(arr)):
        index = get_index(arr, op)
        yield arr.pop(index)


def main():
    lst = [5, 3, 6, 2, 10]
    assert list(selection_sort(lst)) == [2, 3, 5, 6, 10]
    assert list(selection_sort(lst, reverse=True)) == [10, 6, 5, 3, 2]


if __name__ == '__main__':
    main()
