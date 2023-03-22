#  File: Graph.py

#  Description: manipulating graphs

#  Student Name: K. Amber Vasquez

#  Student UT EID: kav835

#  Partner Name: none

#  Partner UT EID: none

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/21/2020

#  Date Last Modified: 11/23/2020

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
  # returns next unvisited vertex, can use in BFs helper
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

    # the stack is empty, let us rest the flags # resets all vertices to be unvsited 
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
  
  def bfs_helper (self,v,queue): 
    # find how many vertices that havent been visited
    
    n = self.get_adj_unvisited_vertex (v) # n returns index in vertices list of the graph 
    while n != -1: 
      self.Vertices[n].visited = True # visited now 
      print (self.Vertices[n])
      queue.enqueue(n)
      n = self.get_adj_unvisited_vertex (v) # resets n until = - 1, when it does, we break out of while loop 
    # out of the while loop, we have visited all the visitis 
    # now we need to dequeue 
    if not queue.is_empty(): 
      m = queue.dequeue()
      self.bfs_helper(m,queue)

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

    
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    # trying to get from vertex to vertex without indexes 
    # we need indexes 
    fromVertexLabel = self.get_index(fromVertexLabel)
    toVertexLabel = self.get_index(toVertexLabel)
    
    if fromVertexLabel == -1 or toVertexLabel == -1: 
      return -1 
    # index into the matrix rows are from 
    edge = self.adjMat[fromVertexLabel,toVertexLabel]
    if edge == 0:
      return - 1
    else: 
      #return edge weight, return what call gave us 
      return edge 

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    
    index = self.get_index(vertexLabel) # returns one index, referes to same vertices , this is the row we need to access 
    neighborList = [] 

    if index == -1: 
      return neighborList 

    # read out the row in the adj matirx that matches that index 
    row = self.adjMat[index]
    for i in range(len(row)): 
      if row[i] != 0: 
        neighborList.append(i)
    return neighborList 


  # get a copy of the list of Vertex objects
  def get_vertices (self):
    return self.Vertices[:]

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    # 0,1 = 1,0 #0,2 = 2,0 
    # acces every possible combo twice  
    # we have a list of all the vertices 
    directed = False 

    for i in range(len(self.Vertices)):
      for j in range(len(self.Vertices)):
        if self.adjMat[i][j] != self.adjMat[j][i]: # we know it is undirected if all are equal 
          directed = True 

    fromIndex = self.get_index(fromVertexLabel) 
    toIndex = self.get_index(toVertexLabel) 

    if directed: #delete a single edge 
      self.adjMat[fromIndex][toIndex] = 0 
  
    else: # undirected 
      self.adjMat[fromIndex][toIndex] = 0
      self.adjMat[toIndex][fromIndex] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
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

def main():
  # create the Graph object
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
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # print the adjacency matrix
  #print ("\nAdjacency Matrix")
  #for i in range (num_vertices):
    #for j in range (num_vertices):
      #print (cities.adjMat[i][j], end = " ")
    #print ()
  #print ()

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()
  #print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  #print (start_index)

  # do the depth first search
  #print ("\nDepth First Search from " + start_vertex)
  print ("\nDepth First Search")
  cities.dfs (start_index)
  
  # test breadth first search
  #print ("\nBreadth First Search from " + start_vertex)
  print ("\nBreadth First Search")
  cities.bfs (start_index)
  print ()

  # test deletion of an edge
  line = sys.stdin.readline()
  twoCities = line.strip().split() 
  cities.delete_edge(twoCities[0], twoCities[1])
  print("Deletion of an edge")
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

  # test deletion of a vertex
  print("Deletion of a vertex")
  line = sys.stdin.readline()
  start_vertex = line.strip()
  cities.delete_vertex(start_vertex)
  print()
  print("List of Vertices")
  for city in cities.Vertices:
    print(city)
  
  print ("\nAdjacency Matrix")
  for i in range (num_vertices-1):
    for j in range (num_vertices-1):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

# in the future len of adj matrix or vertices 



if __name__ == "__main__":
  main()