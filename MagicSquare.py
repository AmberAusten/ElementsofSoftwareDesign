#  File: MagicSquare.py

#  Description: permute through a list and find the versions that are magic squares

#  Student Name: K. Amber Vasquez   

#  Student UT EID: kav835

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/17

#  Date Last Modified: 10/19

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
    n = int(len(a) ** (1/2))
    constant = int(n * (n**2 + 1) / 2)

    newList = [] # want the length of new list to = n
    # indexes through a
    # i in range n takes each row and adds it to new list 
    count = 0
    for i in range (n):
        # builds a row at a time 
        row = []
        for j in range (n):
            row.append(a[j + count])
        #increment it up 
        count += n

        newList.append(row) 

        # a = [1,2,3,4,5,6,7,8,9]
        # newList = [[1,2,3],
        #            [4,5,6],
        #            [7,8,9]]
        # newlist [0][0]
        # change first index, going along the column
        # change the second index, going along the row
    
    for col in range (n):
        s = 0
        # [row][col]
        for row in range(n):
            s = s + newList[row][col] 
        if s != constant:
            return False 
        
    for row in range (n):
        s = 0
        for col in range(n):
            s = s + newList[row][col] 
        if s != constant:
            return False 

    # Left Diagonal 
    # newList [0][0] + newList[1][1] + newList[2][2]
    s = 0
    for row in range (n):
        s = s + newList[row][row]         
    if s != constant:
        return False
    
    # Right Diagonal 
    # newList [0][2] + newList[1][1] + newList[2][0]
    s = 0
    for row in range (n):
        s = s + newList[row][(n-1)-row] 
    if s != constant:
        return False 

    # if newList[0][0] + newList[1][0] + newList[2][0] == constant:
    # for row
    # for col
    # for diagonal 

    return True 

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
    hi = len(a)
    if (idx == hi):
        if is_magic(a):
            b = a[:]
            all_magic.append(b) 
        return       # may need to play with this, might need to happen at bottom 
        #print(a)
    else: 
    # first swap is a swap in place, permute on the rest 
        for i in range(idx,hi):
            a[idx], a[i] = a[i] , a[idx]
            permute (a,idx + 1,all_magic) 
        # swap back to its original configuration 
            a[idx], a[i], = a[i], a[idx]

def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line) #line   
  in_file.close()

  
  # check if you read the input correctly
  #print (n)
  

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  oneDlist = list(range(1, n ** 2 + 1))
  #print(oneDlist)

  # generate all magic squares using permutation 
  permute (oneDlist, 0, all_magic)

  # print all magic squares
  for i in all_magic:
      print(i)  # format later to print out each individual list 

if __name__ == "__main__":
  main()
  #print(is_magic([2,7,6,9,5,1,4,3,8]))
