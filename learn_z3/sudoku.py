
from z3 import *

'''
Positions of the soduko cells:

 0  1  2   3  4  5   6  7  8
 9 10 11  12 13 14  15 16 17
18 19 20  21 22 23  24 25 26

27 28 29  30 31 32  33 34 35
36 37 38  39 40 41  42 43 44
45 46 47  48 49 50  51 52 53

54 55 56  57 58 59  60 61 62
63 64 65  66 67 68  69 70 71
72 73 74  75 76 77  78 79 80
'''

def get_row(cells, r):
    row = []

    for i in range(0, 9):
        idx = 9*r + i
        row.append(cells[idx])

    return row


def get_col(cells, c):
    col = []

    for i in range(0,9):
        idx = 9*i + c
        col.append(cells[idx])

    return col


def get_sqr(cells, s):
    sqr = []

    r = 3 * (s//3)
    c = 3 * (s%3)

    for i in range(0,3):
        for j in range(0,3):
            idx = 9*(r+i) + (c+j)
            sqr.append(cells[idx])

    return sqr

def main():
    # 0 means unknown
    puzzle = [
        9, 4, 0,  0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 2, 0,  0, 6, 0,
        0, 0, 0,  0, 0, 3,  0, 0, 0,

        0, 0, 0,  0, 0, 0,  0, 0, 8,
        0, 2, 0,  0, 0, 0,  4, 0, 9,
        0, 0, 3,  0, 0, 1,  0, 0, 0,

        8, 0, 0,  4, 3, 0,  0, 0, 0,
        0, 0, 7,  0, 0, 0,  0, 1, 0,
        0, 0, 0,  0, 9, 0,  0, 0, 0,
    ]

    cells = [Int("s{}".format(i)) for i in range(0,9*9)]

    axioms = []

    for i in range(0, 9):
        axioms.append(Distinct(get_row(cells, i)))
        axioms.append(Distinct(get_col(cells, i)))
        axioms.append(Distinct(get_sqr(cells, i)))

    for cell in cells:
        axioms.append(1 <= cell)
        axioms.append(cell <= 9)

    for (cell, puzz) in zip(cells,puzzle):
        if puzz != 0:
            axioms.append(cell == puzz)

    solver = Solver()

    solver.add(axioms)

    if (solver.check() == unsat):
        print("Unsolvable.")
        exit(1)

    soln = [0] * 81

    for i in range(0, 81):
        soln[i] = solver.model()[cells[i]].as_long()

    for i in range(0, 9):
        for j in range(0, 3):
            print("{}".format(soln[9*i+j]), end='')

        print(' ', end='')

        for j in range(3, 6):
            print("{}".format(soln[9*i+j]), end='')

        print(' ', end='')

        for j in range(6, 9):
            print("{}".format(soln[9*i+j]), end='')

        print()

        if ((i+1)%3) == 0 and (i+1)!=9:
            print()