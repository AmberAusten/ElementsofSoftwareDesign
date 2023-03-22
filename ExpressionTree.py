#  File: ExpressionTree.py

#  Description:

#  Student's Name: K. Amber Vasquez

#  Student's UT EID: kav835

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 50845

#  Date Created: 11/11/2020

#  Date Last Modified: 11/12/2020


import sys

class Stack (object):
  def __init__ (self):
    self.stack = [] # I'll use a list
    
  
  # add an item to the stack, on the top- PUSH
  def push (self,item): # item can be anything, nubers, strings, objects...
    self.stack.append(item)
  
  # remove an item from the stack, from the top of the stack, POP
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack, examine, 
  def peek (self):
    return self.stack[-1]
      # return does not remove 

  #check if the stack is empty 
  def is_empty (self):
    return len(self.stack) == 0 # returns true if empty 

  # helper function that tells me how big the stack is 
  # return the number of elements in the stack 
  def size (self):
    return len(self.stack)

class Node (object):
  # a point in the tree
  def __init__ (self, data = None): # sets default data to None 
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None 
    # cen set an empty list to hold our pre and post fix stuff 
    # everytime we cal pre and post, reset this list to be empty 
    self.list = [] 

  def create_tree (self, expr): #( ( 8 + 3 ) * ( 7 - 2 ) ) feeds this expression in
    # tokens are any single value 
    exprList = expr.strip().split()
    stack = Stack() # need to create a new stack 
    # set the root value to an empty node 
    self.root = Node() #self.root creates the root, rooot of tree has empty node

    current = self.root 
    #need to do something for each token 
    for i in exprList: # i equal to 
      # If the current token is a left parenthesis 
      if i == "(":
        current.lChild = Node()
        # Push current node on the stack 
        stack.push(current) # current node is just current 
        current = current.lChild
      elif i == ")":
        # check if stack is empty 
        if stack.is_empty() == False:
          current = stack.pop()
      elif i in ["+","*","/","//","%","-","**"]: # operators
        # set the current node's data value to the operator.
        current.data = i #sets it equal to the token 
        stack.push(current)
        # add a new node as the rChild 
        current.rChild= Node()
        # make the current node equal to the right child.
        current = current.rChild
      else: # operands here
        # set the current node's data value to the operand a
        current.data = i
        # make the current node equal to the parent by popping the stack
        current = stack.pop()

  def operate (self,oper1,oper2,token): 
    # create an expression 
    expr = str(oper1) + token + str(oper2) # an infix expression 
    return eval (expr)  # eval is short for evaluate 

  def evaluate (self, aNode): # takes in everything and evaluates it 
    # treee is built in main 
    # call post order, it wll build self.list 
    self.list = [] 
    self.post_order(self.root) # node we have a pointer to 
    # 8 3 + 7 2 - *
    theStack = Stack() 
    
    # define all the operators
    # be exhaustive, Python has no idea what the operators are, symbols I will accept as operators
    operators = ['+','-','*','/','//','%','**'] # redefine cus we are in adifferent scope
    # get a string that is the rPN expression
    
    # identifies operators more quickly 
    # goes through all the tokens in the expression 
    for item in self.list: 
        if (item in operators):
            oper2 = theStack.pop()
            oper1 = theStack.pop() 
            theStack.push(self.operate(oper1,oper2,item)) # pushes the reult of that function to that stack 
        else: # it is not an operator, it is an operand, I push the item
            theStack.push (item) 
    # the very last step is to pop the stack 
    return theStack.pop () # pops off the evaluated answer


  def pre_order (self, aNode):  # Prefix Expression: * + 8 3 - 7 2
    # aNode is just a node. these are recursive functions, calls in one node at a time, appends them to something
    # ANODE IS WHATEVER WE are looking at
    if aNode == None: 
      return None  # when we self.list, self.list isupdated for entire tree , we can call it when we need to acces it 
    else: 
      # youre appending every node onto a list 
      self.list.append(aNode.data) # append into the list
      self.pre_order(aNode.lChild) 
      self.pre_order(aNode.rChild)


  def post_order (self, aNode): # Postfix Expression: 8 3 + 7 2 - *
    # call all the functions then append 
    if aNode == None: 
      return None
    else: 
      self.post_order(aNode.lChild) 
      self.post_order(aNode.rChild)
      self.list.append(aNode.data) # append into the list

      # call all the functions then append 


def main():
  # read infix expression
  line = sys.stdin.readline()
  expr = line.strip()
  # create an empty tree object 
  tree = Tree() 

  # on this varibae we need to call create tree 
  tree.create_tree(expr) 
 
  # evaluate the expression and print the result
  result = float(tree.evaluate(expr))
  print(expr,"=",result)

  # get the prefix version of the expression and print
  tree.list = []
  tree.pre_order(tree.root)
  prefix = " ".join(tree.list)
  print("Prefix Expression:",prefix)

  # get the postfix version of the expression and print
  tree.list = []
  tree.post_order(tree.root)
  postfix = " ".join(tree.list)
  print("Postfix Expression:",postfix)

if __name__ == "__main__":
  main()