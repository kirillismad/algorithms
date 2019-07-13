import math


def partition(sized, part_len):
    parts = math.ceil(len(sized) / part_len)

    for i in range(parts):
        yield sized[i * part_len: i * part_len + part_len]


def main():
    lst = list(range(1, 13))

    for p in partition(lst, 3):
        print(p)


if __name__ == '__main__':
    main()
