#  File: TestBinaryTree.py
#  Student Name: Amber 
#  Date Created: 11/17/2020
#  Date Last Modified: 11/20/2020

# In the class TestBinaryTree you will create several trees 
# and show convincingly that your methods are working. 
# For example you can create a tree by inserting the following 
# integers in this order: 50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96. 
# There should be enough documentation in your code that explains to the student assistants 
# what you are testing and how.
import sys 

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
  # self.parent = None
  # self.visited = False # these are here if you want to add 

class Tree (object):
  def __init__ (self):
    self.root = None # start with an empty tree 

  #search the tree, comparing node to node 
  def inOrder (self, aNode, pNode):

    if (aNode != None and pNode == None) or (aNode == None and pNode != None): 
      return False 

    if (aNode != None) and (pNode != None): 
      if aNode.data != pNode.data: 
        return False 
      return self.inOrder (aNode.lChild, pNode.lChild) and self.inOrder (aNode.rChild,pNode.rChild)
    return True 

  # Returns true if two binary trees are similar
  # that takes as input two binary trees and returns true if the nodes 
  # have the same key values and are arranged in the same order and false otherwise.
  def is_similar (self, pNode): # first node of primary tree 
    
    return self.inOrder(self.root,pNode)


  def level(self,level,location,aNode,aList): 
    
    if aNode == None: 
      return 
    elif level == location: 
      # add thing to list we are keeping track of
      aList.append(aNode.data)  
    else: 
      # recursion calls 
      self.level(level,location + 1, aNode.lChild,aList)
      self.level(level,location + 1,aNode.rChild,aList)

  # Prints out all nodes at the given level
  # takes as input the level and prints out all the nodes at that level. 
  # If that level does not exist for that binary search tree 
  # it prints nothing. Use the convention that the root is at level 1.
  def print_level (self, level): 
    # keep track of what level we are on 
    # and what level we are trying to get to 
    location = 1
    aList = []
    # call helper function 
    self.level(level,location,self.root,aList)
    print(*aList,sep=' ')
    

  def traverse (self,aNode,largest):
    #keep track of largest thing = largest 
    #end 
    if aNode == None: 
      return largest 
    else:
      largest += 1
      return max(self.traverse(aNode.lChild,largest),self.traverse(aNode.rChild,largest)) 
      #returns longest path 
      

  # Returns the height of the tree
  # that returns the height of a binary tree. 
  # Recall that the height of a tree is the longest path length from the root to a leaf.
  def get_height (self): 
    
    return self.traverse(self.root,0)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  # returns the number of nodes in the left subtree from the root and 
  # the number of nodes in the right subtree from the root and the root itself. 
  # This function will be useful to determine if the tree is balanced.
  # * Balance Factor = Height of left sub-tree - Height of right sub-tree
  def count (self,move, aNode): 
   
    if aNode == None: 
      return move - 1
    else:
      move += 1
      move = (self.count(move,aNode.lChild))
      move += 1
      move = (self.count(move,aNode.rChild))
      return move

    
  def num_nodes (self):
    # count left subtree 
    # count right subtree with root included
    leftMove = 0
    rightMove = 0
    if self.root != None: 
      leftMove = self.count(1,self.root.lChild)
      rightMove = self.count(2,self.root.rChild)
    
    return leftMove,rightMove


  def insert (self, ch): # key is fed in here 
    current = self.root 

    #if self.insert(ch)!= "": # if they give duplicates, write search again to make sure not in there
      # ignore the char
      #return 
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

def main():

  # Create three trees - two are the same and the third is different
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree1_input = list (map (int, line)) 	# converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree2_input = list (map (int, line)) 	# converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree3_input = list (map (int, line)) 	# converts elements into ints

  tree1 = Tree() 
  tree2 = Tree()
  tree3 = Tree()

  for i in tree1_input:
    tree1.insert(i) 
  for i in tree2_input:
    tree2.insert(i) 
  for i in tree3_input:
    tree3.insert(i) 

  # Test your method is_similar()
  assert tree1.is_similar(tree2.root) 
  assert (not tree1.is_similar(tree3.root))
  #print("Is Similar passed")

  # Print the various levels of two of the trees that are different
  # print() 
  tree1.print_level(1)
  print()
  tree1.print_level(2)
  print()
  tree3.print_level(3)
  print()
  tree2.print_level(3)
  print()
  

  # Get the height of the two trees that are different
  assert tree1.get_height() == 4
  #print("Height passes")
  assert tree2.get_height() == 4
  #print("Height passes")
  assert tree3.get_height() == 6
  #print("Height passes")


  # Get the total number of nodes a binary search tree
  assert sum(tree1.num_nodes()) == 15
  assert sum(tree2.num_nodes()) == 15 
  assert sum(tree3.num_nodes()) == 15 
  #print("Tree Numbers passed")




if __name__ == "__main__":
  main()
