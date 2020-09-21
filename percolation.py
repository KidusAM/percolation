# *******************************************************
# percolation module
# HW3 Part B
# ENGI E1006
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pdb


def read_grid(input_file):
    """Create a site vacancy matrix from a text file.

    input_file is a file object associated with the
    text file to be read. The method should return
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    dimention = int(input_file.readline())
    grid_list = [[int(value.strip()) for value in line.split(" ")] for line in input_file]
    grid = np.array(grid_list)
    if(grid.shape != (dimention, dimention)): 
        raise RuntimeError("Incorrect file")
    if not (list(np.unique(grid)) in [[0],[1], [0,1]]):
        raise RuntimeError("File isnt only 1s and 0s")
    return grid


def write_grid(filename, sites):
    """Write a site vacancy matrix to a file.

    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    with open(filename, 'w') as written_file:
        written_file.write(str(len(sites)) + "\n")
        np.savetxt(written_file, sites,fmt="%d" )


def percolate(mat, x, y):
    ''' Recursively simulates the percolation of liquid in a grid '''
    if(mat[y, x] == 1): mat[y,x] = 2 #base case
    y_dim, x_dim = mat.shape
    left = (x>0) and (mat[y, (x-1)] == 1) #left percolation allowed
    right = (x<x_dim-1) and (mat[y, x+1] == 1) #right perc allowed
    down = (y<y_dim-1) and (mat[y+1,x] == 1) #down perc allowed
    
    if(left): percolate(mat, x-1, y)
    if(right): percolate(mat, x+1, y)
    if(down): percolate(mat, x, y+1)
    


def flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This
    function should return the corresponding flow matrix generated
    through vertical percolation
    """
    percolated = sites.copy()
    for i, item in enumerate(sites[0]):
        if(item == 1): 
            percolate(percolated,i, 0)
    return percolated
    
 

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    return 2 in flow_matrix[-1]


def make_sites(n, p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy
    matrix with site vaccancy probability p
    """
    random = np.random.rand(n,n)
    site = (random<(p)).astype(int)
    return site


def plot(before, after):
    """Plots the before and after matrices using matplotlib
    """
    fig, axes = plt.subplots(1, 2)

    axes[0].pcolor(before, cmap='Greys_r')
    axes[0].set_ylim(before.shape[0], 0)

    l = ListedColormap(['black', 'white', 'blue'])
    axes[1].pcolor(after, cmap=l)
    axes[1].set_ylim(before.shape[0], 0)
    plt.show()
