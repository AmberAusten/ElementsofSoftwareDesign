#  File: Chess.py

#  Description:

#  Student Name: K. Amber Vasquez   

#  Student UT EID: kav835

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/20

#  Date Last Modified: 10/23

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    count = 0

    if (col == self.n):
      return 1
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          count += (self.recursive_solve(col + 1)) 
            #return True
          self.board[i][col] = '*'
      return count

  # if the problem has a solution print the board
  def solve (self):
      return (self.recursive_solve(0)) # giving u thie first one that works, returning true 
        #self.print_board()

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)
  
  #for i in range(1,13):
    #game = Queens(i)
    #print(game.solve())
  
  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  #game.solve()

  # print the number of solutions
  print(game.solve())
 
if __name__ == "__main__":
  main()
