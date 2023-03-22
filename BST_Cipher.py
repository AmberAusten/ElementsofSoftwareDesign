#  File: BST_Cipher.py

#  Description: encrypts and decrypts a string using a BST 

#  Student Name: K.Amber Vasquez

#  Student UT EID: kav835

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/12/2020

#  Date Last Modified:11/14/2020



import sys

class Node (object):
  # a point in the tree
  def __init__ (self, data = None): # sets default data to None 
    self.data = data
    self.lChild = None
    self.rChild = None
# To encode a sentence, insert each letter into a binary tree using the ASCII value as a comparative measure.
# For this assignment we are only going to encrypt lower case letters "a" through "z" and the space character.
class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None 
    self.encrypt_str = encrypt_str

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch): # key is fed in here 
    current = self.root 

    if self.search(ch)!= "":
      # ignore the char
      return 
    aNode = Node(ch) # aNode is the specific instance that has the data value ch
    while current != None:
      if ch < current.data: # we need to check before we move 
        if current.lChild == None:
          current.lChild = aNode 
          return
        current = current.lChild 
      else: 
        if current.rChild == None:      
          current.rChild = aNode   
          return 
        current = current.rChild
    # insert at the root
    self.root = aNode 
    return
    
    # test if it already exists 
    # could use a set ( dont care about duplicates)
    # check if sentense is in set, (letter)
    #OR
    # call search on character 
    # if blank, insert, if not blank, insert it 

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch): # st we want to encrypt 
    current = self.root 
    string = ""
    # look at first one , the root, if its not equal to it, if greater than look at chilf then less than look at left
    # if we search through all the way, get to a node that is None 
    if self.root == None: 
      return ""
    if self.root.data == ch:
      return "*"
    while current != None: # doesn't check only yhe root 
      if ch == current.data:
        return string 
      if ch < current.data: 
        string += "<"
        current = current.lChild 
      else: 
        string += ">"
        current = current.rChild
    return ""

    # we write this first 
    # preorder/post order traversals
    # keep track of how many lefts and rights we do 
        # when you go the left child, call search on left child
    # write a helper a fuction to do the traversal feed it in root at beginning 
    # left count and right count 
    # get search working 


  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st): #st we want to decrypt st by st
    # we have pre and post order
    # takes in a string from search?, ex: "<,>,<,<,<"
    current = self.root 

    for i in st:
      if current == None:
        return ""
      elif i == "<":
        current = current.lChild 
      elif i == ">":
        current = current.rChild 
    return current.data


    # follows the patterns it gives, <,>,etc
    # we are traversing through the tree
    # write it out in a specific way to use the left and right arrows 
  
    # returns the corresponding character in the tree or an empty string the character isnt found

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  # the quick brown fox jumps over the lazy dog.
  def encrypt (self, st): # feed in ch by ch into search 
    # takes a lowercase string and converts it using encryption using
    #searches for each individual ch in tree and returns very long string
    #ch by ch, returns a long string with the left and right arrows 
    
    st = st.lower() 
    s = ""
           
    for i in st:
      s += self.search(i) # returns all the arrows that got us to the letter
      if self.search(i) == "":
        # skip 
        continue 
      s += "!"
    s = s[:-1]

    return s


  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string. # <><>><<<!<><>>!<><>><!<<>>!<!<><>>!<>>!<><>>< returns a normal
  def decrypt (self, st):
    # split by ! 
    st = st.split("!") #saves it as a list of these <,>,*
    string = ""

    for i in st: 
      string += self.traverse(i)
    
    return string 


    

# "the quick brown fox jumps over the lazy dog". key
# gives you all the letter you need for encryption 
# need binary search tree and all your functions for that 
def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  for i in encrypt_str:
    the_tree.insert(i)
  
  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
  
 
if __name__ == "__main__":
  main()