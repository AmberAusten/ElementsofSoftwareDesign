#  File: TopoSort.py

#  Description:

#  Student Name: K. Amber Vasquez

#  Student UT EID: kav835

#  Partner Name: none   

#  Partner UT EID: none 

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/25/2020

#  Date Last Modified: 11/29/2020


import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Edge (object):
    pass 

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    newQueue = Queue () # create an empty queue
    print(self.Vertices[v])
    #we are starting at V, set starting one to be visited
    self.Vertices[v].visited = True
    #visit all the nodes in the graph, every adjacent vertices in a specific order
    # as we visit add them to a queue 
    # then dequeue
    self.bfs_helper(v,newQueue)
    
    #resets all vertices to be unvisited
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # our helper function is going to take in a vertex, 
  # the first thing you want to do is see if the vertex has been visited to
  def has_cycle_helper (self,v):
    # return true if the vertex has been visited - base case 1 
    # return false if the vertex has no neighbors (out degree is 0) - base case 2 marke as visited
    # to have a cycle, it has to have at least one out degree 
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = False
    #print (self.Vertices[v])
    theStack.push (v)

    newList = []
    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        newList.append(self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    
    return newList
    
    
    # loop through the neighbors of the vertex, call helper on each neighbors 
    #for v in neighbors: 
      #return has_cycle_helper(v) # return whatever it returns 
      
  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
      # lop through the vertices
    for vert in range(len(self.Vertices)): 
      # for eachvertex, cal helper function 
      cycle = self.has_cycle_helper(vert) # this will have the list, see if the vert is in here twice
      if self.Vertices[vert] in cycle[1:]:
        return True
    return False 


  def delete_vertex (self, vertexLabel):
    # delete an entire row and column from adj matrix 
    # find index of label 
    index = self.get_index(vertexLabel)
    if index == -1: 
      return 
    # remove row from a 2dList 
    self.adjMat.pop(index) 
    #remove column
    for i in self.adjMat : # i will = every row in the adj matrix 
      i.pop(index) # removes from adj mat
    
    # adj mat reset 
    self.Vertices.pop(index)

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    #Works on directed graphs that do not have cycles (DAGs)
    # empty dictionary 
    
    queue = Queue()

    while self.Vertices != []:
      inDegree = {}
      for i in range(len(self.Vertices)): # gets the indexes, = column we are looking at (i is the index of the col we need to look)
        in_degrees = 0 
        for j in self.adjMat: #j is the row
          if j[i] > 0:
            in_degrees += 1
        inDegree[self.Vertices[i].label] = in_degrees # creates the key 

      # every single vertices assigned to its indegree in dictionary 
      zeroList = [] 
      for i in inDegree: # i will equal the key 
        if inDegree[i] == 0: 
          zeroList.append(i) # key is the label
          self.delete_vertex(i) # deletes vertex 
      zeroList.sort()

      for i in zeroList:
        queue.enqueue(i)

    vertexLabels = [] 
    for i in range(queue.size()): # equals the list in the queue 
      dq = queue.dequeue()
      #print(dq)
      vertexLabels.append(dq)
    
    return vertexLabels 

    # 0. Determine the in_degree for all vertices. The in_degree is
    #the number of edges that are incident on that vertex.

    # 1. Remove the vertices that have an in_degree of 0 to a list and
     #remove the out going edges from those vertices. Sort the list
     #in a given order. Enqueue the vertices into a Queue and then 
     #update the in_degree of all remaining vertices.

    # 2. Repeat step 1 until there are no more vertices in the Graph.

    # 3. Dequeue the vertices and print.
  
    # return a list of vertex labels 

    

def main():
  # create a Graph object
  cities = Graph()
  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    #print (city)
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  #print (num_edges)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    #print (edge)
    edge = edge.split()
    start = cities.get_index(edge[0])
    finish = cities.get_index(edge[1])
    weight = 1

    cities.add_directed_edge (start, finish, weight)

  # test if a directed graph has a cycle
  if (cities.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  if (not cities.has_cycle()):
    vertex_list = cities.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)

main()

