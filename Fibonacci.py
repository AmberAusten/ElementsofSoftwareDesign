# File: Fibonacci.py

# Description: 

# Student's Name: K. Amber Vasquez  

# Student's UT EID: kav835

# Partner's Name:

# Partner's UT EID:

# Course Name: CS 313E

# Unique Number: 50845

# Date Created: Oct 7

# Date Last Modified: Oct 8

import sys # added import sys 11/13/2020 
# Input: n a positive integer
# Output: a bit string

def f(n):

    if n == 0: 
        return "0"
    elif n == 1:
        return "1"
    else: 
        return f(n-1) + f(n-2)

# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):
    lengthP = len(p)
    count = 0
    for i in range(len(s)):             # I do want the index, feed range an int
        if s[i:lengthP + i] == p:
            count += 1
    
    return count 

def main():
  
  # read n and p from standard input: user input 
    #n = int(input("n: "))
    #p = input("p: ")
  # read n and p from standard input: reading fib.in 
    #infile = open("fib.in", "r") 
    #n = int(infile.readline().strip())
    #p = (infile.readline().strip())

  # read n and p from standard input: Mitra's code update
    n = sys.stdin.readline()
    n = int (n.strip())
    p = sys.stdin.readline()
    p = p.strip()

  # compute the bit string f(n)
    s = f(n)

  # determine the number of occurrences of p in f(n)
    numOccurrences = count_overlap(s,p)

  # print the number of occurrences of p in f(n)
    print(numOccurrences)

if __name__ == "__main__":
  main()