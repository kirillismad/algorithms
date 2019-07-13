def euclidean_algorithm(a, b):
    if a % b == 0:
        return b
    return euclidean_algorithm(b, a % b)


def inf_euclidean_algorithm(*args):
    if len(args) == 2:
        return euclidean_algorithm(*args)
    return inf_euclidean_algorithm(euclidean_algorithm(args[0], args[1]), *args[2:])


def main():
    assert euclidean_algorithm(1071, 462) == 21
    assert inf_euclidean_algorithm(570, 294, 78, 36) == 6


if __name__ == '__main__':
    main()
