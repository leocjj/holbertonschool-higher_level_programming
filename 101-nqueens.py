#!/usr/bin/python3
""""Module to define a rectangle class"""


from sys import argv

def print_chess(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(' {:2.0f} '.format(m[i][j]), end='')
        print()

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    nqueens = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1);

if not isinstance(nqueens, int):
    print('N must be a number')
    exit(1)

if nqueens <= 4:
    print('N must be at least 4')
    exit(1)

m = []
row = []
for i in range(nqueens):
    for j in range(nqueens):
        row += [j]
    m += [row]
    row = []

ri = 0
rj = 0

for ri in range(5):
    for rj in range(nqueens):
        if m[ri][rj] >= 0:
            m[ri][rj] = -2
            break;
    # Clear column
    for i in range(nqueens):
        if i != ri:
            m[i][rj] = -1
    # Clear row
    for j in range(nqueens):
        if j != rj:
            m[ri][j] = -1
    # Clear diagonal / up
    for d in range(1, nqueens):
        if (ri + d) < nqueens and (rj + d) < nqueens:
            m[ri + d][rj + d] = -1
        else:
            break
    # Clear diagonal / down
    for d in range(1, nqueens):
        if (ri - d) < nqueens and (rj - d) < nqueens:
            m[ri - d][rj - d] = -1
        else:
            break
    # Clear diagonal \ up
    for d in range(1, nqueens):
        if (ri + d) < nqueens and (rj - d) < nqueens:
            m[ri + d][rj - d] = -1
        else:
            break
    # Clear diagonal / up
    for d in range(1, nqueens):
        if (ri - d) < nqueens and (rj + d) < nqueens:
            m[ri - d][rj + d] = -1
        else:
            break

print_chess(m)
