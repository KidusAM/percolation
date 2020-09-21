# *******************************************************
# HW 3
# ENGI E1006
# *******************************************************
import numpy as np

import percolation as perc


def main():
    A = perc.make_sites(25, 0.65)
    perc.write_grid('test.txt', A)
    infile = open('test.txt', 'r')
    B = perc.read_grid(infile)
    C = perc.flow(B)
    #print(B)
    #print(C)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    perc.plot(B, C)

if __name__ == "__main__":
    main()
