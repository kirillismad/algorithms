from random import shuffle


def qsort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        greater = [x for x in lst[1:] if x > pivot]

        return qsort(less) + [pivot] + qsort(greater)


def main():
    lst = list(range(1000))
    shuffle(lst)
    print(qsort(lst))


if __name__ == '__main__':
    main()
