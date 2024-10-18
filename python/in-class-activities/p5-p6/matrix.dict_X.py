import random

MR = 7
MC = 7


def create_matrix(mr, mc, seq):
    matrix = {}
    matrix['max_rows'] = mr
    matrix['max_columns'] = mc

    '''
    # Exception
    if len(seq) != mr * mc:
        err = f"Sequence size {len(seq)} doesn't match "\
            f"the matrix size {mr}x{mc}\n"
        raise ValueError(err)
    '''
    matrix['seq'] = []
    if len(seq) < mr * mc:
        msg = f"WARNING: The sequence is shorter " \
              f"than the matrix size\nFILLING with zeros\n"
        print(msg)
        for i in range(len(seq)):
            matrix['seq'].append(seq[i])
        for i in range(mr * mc - len(seq)):
            matrix['seq'].append(0)
        # matrix['seq'] += [0]* (mr * mc - len(seq))
        # matrix['seq'].extand([0]* (mr * mc - len(seq)))
    elif len(seq) > mr * mc:
        msg = f"WARNING: The sequence is longer " \
              f"than the matrix size\nTRUNCATING\n"
        print(msg)
        for i in range(mr * mc):
            matrix['seq'].append(seq[i])
    else:
        for i in range(len(seq)):
            matrix['seq'].append(seq[i])

    return matrix


def print_matrix(matrix):
    mr = matrix['max_rows']
    mc = matrix['max_columns']
    seq = matrix['seq']

    max_width = max(map(len, map(str, seq)))

    s = "\n"
    for row in range(mr):
        for col in range(mc):
            i = matr2vect(matrix, row, col)
            s += f"{seq[i]:^{max_width + 3}}"
        s += '\n' * 2

    return s


def matr2vect(matrix, r, c):
    mr = matrix['max_rows']
    mc = matrix['max_columns']

    if type(r) != int or type(c) != int:
        raise TypeError

    if 0 > r or r > mr - 1 or 0 > c or c > mc - 1:
        raise IndexError

    i = r * mc + c

    return i


def vect2matr(matrix, i):
    mr = matrix['max_rows']
    mc = matrix['max_columns']

    if type(i) != int:
        raise TypeError

    if 0 > i or i > mr * mc - 1:
        raise IndexError

    r = i // mc
    c = i % mc

    return r, c


def get_matrix_value(matrix, r, c):
    i = matr2vect(matrix, r, c)
    return matrix['seq'][i]


def set_matrix_value(matrix, r, c, value):
    i = matr2vect(matrix, r, c)
    matrix['seq'][i] = value


def main():
    '''
Matrix testing

Returns
-------
None.

'''

    s = [random.randint(1, 1000) for i in range(1, 50)]
    m = create_matrix(MR, MC, s)
    s = print_matrix(m)
    print(s)

    res = get_matrix_value(m, 0, 0)
    print(res)

    set_matrix_value(m, 0, 0, -100)
    s = print_matrix(m)
    print(s)


if __name__ == '__main__':
    main()