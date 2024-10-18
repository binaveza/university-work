import random
import math

MR = 7
MC = 7


class Matrix:
    precision = 2

    def __init__(self, mr, mc, seq):

        self.max_rows = mr

        # self.__dict__['max_columns'] = mc
        # self.max_Columns = mc
        setattr(self, 'max_columns', mc)

        array = []
        if len(seq) < mr * mc:
            msg = "WARNING: The sequence is shorter " \
                  "than the matrix size\nFILLING with zeros\n"
            print(msg)
            for i in range(len(seq)):
                array.append(seq[i])
            for i in range(mr * mc - len(seq)):
                array.append(0)
            # matrix['seq'] += [0]* (mr * mc - len(seq))
            # matrix['seq'].extand([0]* (mr * mc - len(seq)))
        elif len(seq) > mr * mc:
            msg = "WARNING: The sequence is longer " \
                  "than the matrix size\nTRUNCATING\n"
            print(msg)
            for i in range(mr * mc):
                array.append(seq[i])
        else:
            for i in range(len(seq)):
                array.append(seq[i])

        self.seq = array

    def __str__(self):
        mr = self.max_rows
        mc = self.max_columns
        seq = self.seq

        max_width = max(map(len, map(str, seq))) + Matrix.precision + 1

        s = "\n"
        for row in range(mr):
            for col in range(mc):
                i = self.matr2vect(row, col)
                s += f"{seq[i]:^{max_width + 3}.{Matrix.precision}f}"
            s += '\n' * 2

        return s

    def matr2vect(self, r, c):
        mr = self.max_rows
        mc = self.max_columns

        if type(r) != int or type(c) != int:
            raise TypeError

        if 0 > r or r > mr - 1 or 0 > c or c > mc - 1:
            raise IndexError

        i = r * mc + c

        return i

    def vect2matr(self, i):
        mr = self.max_rows
        mc = self.max_columns

        if type(i) != int:
            raise TypeError

        if 0 > i or i > mr * mc - 1:
            raise IndexError

        r = i // mc
        c = i % mc

        return r, c

    def get_matrix_value(self, r, c):
        i = self.matr2vect(r, c)
        # return self.__dict__['seq'][i]
        return self.seq[i]

    def set_matrix_value(self, r, c, value):
        i = self.matr2vect(r, c)
        # self.__dict__['seq'][i] = value
        self.seq[i] = value

    def __getitem__(self, item):
        print(item, type(item))

        mr = self.max_rows
        mc = self.max_columns

        if type(item) not in (int, tuple, slice):
            raise TypeError

        if type(item) == int:
            row = self.get_row_seq(item)
            res = Matrix(1, mc, row)
        elif type(item) == tuple:
            if len(item) != 2:
                raise ValueError
            else:
                a = item[0]
                b = item[1]
                if type(a) == int:
                    if type(b) == int:
                        res = self.get_matrix_value(a, b)
                    elif type(b) == slice:
                        row = self.get_row_seq(a)[b]
                        res = Matrix(1, len(row), row)
                    else:
                        raise ValueError
                elif type(a) == slice:
                    rows = [i for i in range(mr)][a]
                    array = []
                    for r in rows:
                        if type(b) == int:
                            row = [self.get_row_seq(r)[b]]
                        elif type(b) == slice:
                            row = self.get_row_seq(r)[b]
                        else:
                            raise ValueError
                        array.extend(row)
                    res = Matrix(len(rows), len(row), array)
        elif type(item) == slice:
            rows = [i for i in range(mr)][item]
            array = []
            for r in rows:
                row = self.get_row_seq(r)
                array.extend(row)
            res = Matrix(len(rows), mc, array)
        else:
            raise ValueError

        return res

    def get_row_seq(self, r):
        mr = self.max_rows
        mc = self.max_columns

        if 0 > r or r > mr - 1:
            raise IndexError
        else:
            row = []
            for c in range(mc):
                i = self.matr2vect(r, c)
                row.append(self.seq[i])

        return row

    def sqrt(self, p=6):
        mr = self.max_rows
        mc = self.max_columns

        seq = list(map(math.sqrt, self.seq))
        seq = list(map(lambda x, p=p: round(x, p), seq))
        return Matrix(mr, mc, seq)


def main():
    '''
Matrix testing

Returns
-------
None.

'''

    s = [random.randint(1, 1000) for i in range(1, 50)]
    m = Matrix(MR, MC, s)
    print(m.__dict__)
    print(m)

    res = m.get_matrix_value(0, 0)
    print(res)

    m.set_matrix_value(0, 0, -100)
    print(m)

    Matrix.precision = 2

    m1 = m[1:4, 1:4]
    print(m1)
    print(m1.sqrt())

    print(m1.precision)


if __name__ == '__main__':
    main()