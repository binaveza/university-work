MR = 10
MC = 10

def create_matrix(mr, mc, seq):
    matrix = {}
    matrix['max_rows'] = mr
    matrix['max_colums'] = mc
    matrix['seq'] = seq

    # eXCEPTION
    if len(seq) != mr * mc:
        err = f"sequence size {len(seq)} does not match the matrix size {mr}x{mc}\n"
        raise ValueError(err)

    return matrix

def main():
    '''
Matrix testing
:return:
NONE
'''

    s = [i for i in range(100)]
    m = create_matrix(MR, MC, s)

if __name__ == '__main__':
    main()