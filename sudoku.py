import numpy as np
import math

grid = np.array(
[
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
], np.uint8)

def could_go_in(num, cell, grid, n, n2): #num is an integer, cell is a tuple(r,c), grid is an array 
    '''Check if a number could go in a cell by seeing if it's row/col/box already has this number.'''
        
    #check that cell is not 0
    if grid[cell[0]][cell[1]] != 0:        
        return False
    #check that the row and col is clear
    for i in range(n2):
        if grid[cell[0]][i] == num:
            return False
        if grid[i][cell[1]] == num:
            return False
    #check that box is clear
    br, bc = (cell[0]//3)*3, (cell[1]//3)*3
    for i in range(n):
        for j in range(n):
            if grid[br + i][bc + j] == num:
                return False
    return True

def analytical_solve(grid, n, n2):
    '''Solve the grid analyticaly in two different ways once, repetition of this approach is needed '''

    '''For each row/col/box if there is only one place for a number to go put it there'''
    

    '''For each cell if there is only one number that can go in there put it there'''
    for i in range(n2):
        for j in range(n2):
            pos = 0 # possible number
            amount = 0 # amount of possible numbers
            for k in range(1, n2+1):
                if could_go_in(k, (i, j), grid, n, n2):
                    pos, amount = k, amount+1
                if amount > 1:
                    break
            if amount == 1:
                grid[i][j] = pos

    return grid

def full_analytical_solve(grid, n, n2):
    '''Iterate the analytical solve until it is no longer possible'''
    for i in range(n2**2+1):
        old_grid = np.array(grid)
        grid = analytical_solve(grid, n, n2)
        if np.array_equal(grid, old_grid):
            print("{} iterations".format(i))
            return grid
        
def solve_sudoku(grid):
    
    #check that the grid has correct dimensions
    assert grid.shape[0] == grid.shape[1], "Grid is not square"
    assert math.sqrt(grid.shape[0]) % 1 == 0, "Grid has non-square side lengths"

    #Set the dimensions to be used in the rest of the program
    n = int(math.sqrt(grid.shape[0]))
    n2 = n**2

    #run for 1000 iterations
    for i in range(3000):
        old_grid = np.array(grid)
        grid = full_analytical_solve(grid, n, n2)
        if np.array_equal(grid, old_grid):
            print("{} iterations".format(i))
            break

    print_sudoku(grid)

def print_sudoku(grid):
    n = int(math.sqrt(grid.shape[0]))
    for i in range(n**2 ):
        if (i/3)%1 == 0:
            print("")
        print_line = ""
        for j in range(n**2):
            if (j/3)%1 == 0:
                print_line += "  "
            print_line += str(grid[i][j]) + " "
        print(print_line)

solve_sudoku(grid)

    
