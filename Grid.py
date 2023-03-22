
#  File: Grid.py

#  Description: prints total number of paths in the grid and greatest path sum in the grid

#  Student Name: K. Amber Vasquez

#  Student UT EID: kav835

#  Partner Name: Nicole Fox Estabrook

#  Partner UT EID: nae588

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created:

#  Date Last Modified: 10/30/2020

import sys
import math

def make_grid(n):
 
    grid = [] 
    for i in range (n):
        row = [] 
        for j in range (n):
            row.append(0)
        grid.append(row)
    
    return grid

# counts all the possible paths in a grid 
def count_paths (n):
    side = n
    numSteps = 2 * (side-1)
    numStepsRight = numSteps//2

    sumPaths = math.factorial(numSteps)//(math.factorial(numStepsRight) * math.factorial(numSteps-numStepsRight))

    return(int(sumPaths))

# gets the greatest sum of all the paths in the grid
def path_sum (grid, n):

    sum_grid = make_grid(n)
    
    i = n-1
    j = n-1

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == n-1 and j == n-1:
                sum_grid[i][j] = int(grid[i][j])
            elif i == n-1 or j == n-1:
                if i == n-1:
                    sum_grid[i][j] = int(grid[i][j]) + sum_grid[i][j+1]
                elif j == n-1:
                    sum_grid[i][j] = int(grid[i][j]) + sum_grid[i+1][j]
            else: #guts
                if sum_grid[i+1][j] >= sum_grid[i][j+1]:
                    sum_grid[i][j] = int(grid[i][j]) + sum_grid[i+1][j]
                elif sum_grid[i][j+1] > sum_grid[i+1][j]:
                    sum_grid[i][j] = int(grid[i][j]) + sum_grid[i][j+1]

    return(sum_grid[0][0])

def main():
  # read the dimension of the grid
  line = sys.stdin.readline()
  line = line.strip()
  dim = int (line)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    row = list (map (int, line))
    grid.append (row)

  '''
  # print the grid
  print (grid)
  '''

  # get the number of paths in the grid and print
  num_paths = count_paths (dim)
  print (num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim)
  print (max_path_sum)

if __name__ == "__main__":
  main()
