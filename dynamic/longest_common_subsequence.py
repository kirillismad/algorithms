from collections import namedtuple

Elem = namedtuple('Elem', ['len', 'result'])


def lcs_no_recursion(s1, s2):
    M = [[Elem(0, '') for __ in s2] for _ in s1]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                M[i][j] = Elem(M[i - 1][j - 1].len + 1, M[i - 1][j - 1].result + s1[i])
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1], key=lambda elem: elem.len)

    return M[-1][-1].result


def lcs_no_recursion_2(s1, s2):
    L = [[0 for __ in s2] for _ in s1]

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs = ''
    s1_i, s2_i = len(s1) - 1, len(s2) - 1
    while s1_i >= 0 and s2_i >= 0:
        if s1[s1_i] == s2[s2_i]:
            lcs += s1[s1_i]
            s1_i, s2_i = s1_i - 1, s2_i - 1
        elif L[s1_i - 1][s2_i] > L[s1_i][s2_i - 1]:
            s1_i -= 1
        else:
            s2_i -= 1

    return lcs[::-1]


def main():
    s1 = 'sh'
    s2 = 'osh'
    s3 = 'losh'
    print(lcs_no_recursion_2(s2, s3))


if __name__ == '__main__':
    main()
