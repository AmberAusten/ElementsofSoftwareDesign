#  File: TestLinkedList.py

#  Description: Create many methods to work with Linked Lists

#  Student Name: K. Amber Vasquez

#  Student UT EID: kav835

#  Partner Name: Nicole Estabrook

#  Partner UT EID: nae588

#  Course Name: CS 313E

#  Unique Number: 50845 

#  Date Created: 11/3/2020

#  Date Last Modified: 11/6/2020


class Link (object): 
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next 

class LinkedList (object):
  # create a linked list
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    
    i = 0 # counter
    currentLink = self.first # link objects have the next atribute associated with them
    # stop when currentLink == None 
    while currentLink != None:
      currentLink = currentLink.next # find the attribute 'next' in this object and assign it to the current link 
      i += 1

    return i
      
  # add an item at the beginning of the list
  def insert_first (self, data): 
    # whenever I want to insert, I need to create new link, always 
    new_link = Link(data) # new link is an address 

    new_link.next = self.first # point to this to be next 
    self.first = new_link # self.first gets the address of the new_link, resets self.first to the new_link 

  # add an item at the end of a list
  def insert_last (self, data): 
    new_link = Link (data) # creats a lunk with the data 
    # how do i know I have reached the last link? When next field is None
    # lets start at the beginning 
    current = self.first
    if (current == None): # means the link list is empty 
        # if it is an emtpy list, does it makes ense to add to the end? No 
        self.first = new_link
        return 
    # now I know where I am is not empty cus I already tested it above 
    while (current.next != None): 
        # go to the next link, this is code that gets us to the next link 
        current = current.next
    # now I get out of the loop, I have gotten to the last link, the one line of code I need
    current.next = new_link 

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data): 
    # whenever I want to insert, I need to create new link, always 
    new_link = Link(data) # new link is an address 
    current = self.first

    if (current == None): # means the link list is empty 
      # if it is an emtpy list, does it makes ense to add to the end? No 
      self.first = new_link
      return 
    
    while (current.next != None):
      if current.next.data < data: 
        current = current.next
      else: 
        new_link.next = current.next
        current.next = new_link 
        return
    else:
      current.next = new_link 

    
  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    # start from beginning as always 
    current = self.first 

    # a special case I always need to take care of is if the list is empty 
    # if it is empty, I really cannot find anything 
    if (current == None):
        return None 
    # otherwise, I am going link by link 
    while (current.data != data): 
        if (current.next == None): # we have reached the end of the list and have not found it 
            return None 
        else: # i want to go to the next link 
            current = current.next 
    # if I am where the cursor is now, we have found it 
    # we want to return the link where we found the data 
    return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): # ordered is sorted, if links will contain numbers, numerical order
    # can do binary search 
    # iterate through the linked list and put all of it in an actual list 
                    # OR # 
    # start at first node, if < thing, move to next node
    # when you hit a grater one, return that its not there
    # node to node using the linked element
    current = self.first 

    if (current == None):
        return None 
    # otherwise, I am going link by link 
    while (current.data != data): 
        if (current.next == None): # we have reached the end of the list and have not found it 
            return None 
        elif current.data > data: 
            return None 
        else:
          current = current.next
    
    return current 


  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    
    previous = self.first 
    current = self.first 

        # special case, it is an empty list 
    if current == None: 
      return None
        
  # look for the data 
    while current.data != data: 
      if (current.next == None):
        return None 
      else: 
        previous = current 
        current= current.next
        # when I get out, I have found it
        # if it is the first link :
      if current == self.first: 
        self.first = self.first.next    # delete the first link 
        # it is not the first link, what do i do next? 
      else: 
        previous.next = current.next
        
    return current 

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
  # return all the different data points into one string 
  # iterate through
    currentLink = self.first # link objects have the next atribute associated with them
    # stop when currentLink == None 
    string = ""
    i = 0
    while currentLink != None: 
      string += str(currentLink.data) + "  "
      i += 1
      currentLink = currentLink.next
      # when i == 10, add \n character 
      if i == 10:
        string += "\n"
        i = 0
    return string
    
  # Copy the contents of a list and return new list
  def copy_list (self):

    linkedList = LinkedList()
    current = self.first 

    while current != None:
      linkedList.insert_last(current.data)
      current = current.next
    return linkedList


  # Reverse the contents of a list and return new list
  def reverse_list (self): 
    linkedList = LinkedList()
    current = self.first 

    while current != None:
      linkedList.insert_first(current.data)
      current = current.next
    return linkedList

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self): 
    # take all the points, put them in a normal list, calling sorted on it, 
    # and then creating a new link list with the new sorted points in it 
   
    toList = [] 
    index = 0
    current = self.first

    while current != None:
      toList.append(current.data)
      current = current.next
    sortedToList = sorted(toList)

    # create a new linked list object 
    newLinkedList = LinkedList()
    # take all the values in sorted t list and call insert last on them 
     # we want every item in this list tot be its own link 
    for i in sortedToList: # points to actual data
      newLinkedList.insert_last(i) # asking nLL< can you insert this value last

    return newLinkedList


  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    # conditionals, if this is less than that, all the way up 
    current = self.first 
    if (current == None):
        return None 
    # otherwise, I am going link by link 
    while (current.next != None): # current.nexy is the link object
        if current.data > current.next.data: 
          return False 
        else:                                   # current.data <= current.next.data: 
          current = current.next 
    return True
  
  # Return True if a list is empty or False otherwise
  def is_empty (self): 

    return self.first == None      

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other): # **
    # create a regular list from a LL
    toList = [] 
    index = 0
    current = self.first

    while current != None and current.next != None:
      toList.append(current.data)
      current = current.next
    
    index = 0
    current = other.first
    while current != None:
      toList.append(current.data)
      current = current.next

    # toList
    print("toList before linked:",toList)
    # create a new linked list from the toList merged
    newLinkedList = LinkedList ()
    for i in toList: # points to actual data
      newLinkedList.insert_last(i) 

    return newLinkedList.sort_list()


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    toList = [] 
    index = 0
    current = self.first

    while current != None:
      toList.append(current.data)
      current = current.next
    
    toList2 = []
    index = 0
    current = other.first
    while current != None:
      toList2.append(current.data)
      current = current.next

    return toList == toList2 

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self): # ** 
    toList = [] 
    index = 0
    current = self.first

    while current != None:
      if current.data not in toList: 
        toList.append(current.data)
      current = current.next

      # toList will return the first occurance 

    newLinkedList = LinkedList ()
    for i in toList: # points to actual data
      newLinkedList.insert_last(i) 

    return newLinkedList
    

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  # create a linked list object 
  linkedList = LinkedList () # all object saved as LL
  #insert more than 10 items
  for i in range(10): # 
    linkedList.insert_first(i) # inserts i every single time, puts all the numbers 0-10 into a LL 
  print("")
  print ("Insert first",str(linkedList),"\n")

  # Test method insert_last()
  linkedList = LinkedList () # all object saved as LL
  for i in range(10): # 
    linkedList.insert_last(i)
  
  #linkedList.insert_last(10)
  print ("Insert last",str(linkedList),"\n")

  #print(linkedList) #autocalls string
  # Test method insert_in_order()
  linkedList = LinkedList () # all object saved as LL
  for i in range(10): 
    if i % 2 == 0:
      linkedList.insert_in_order(i)
  linkedList.insert_in_order(5)
  print("Insert in Order:",linkedList,"\n")
  

  # Test method get_num_links()
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_in_order(i)
  print("NumLinks:",linkedList.get_num_links(),"\n")

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_last(i)
  print("Find unordered there link:",linkedList.find_unordered(2))
  print("Find unordered not there:",linkedList.find_unordered(20),"\n")

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_last(i)
  #print("Ordered",linkedList.find_ordered())
  print("Find ordered there link is:",linkedList.find_unordered(2))
  print("Find ordered not there:",linkedList.find_unordered(20),"\n")

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_last(i)
  print("Delete link data there:",linkedList.delete_link(2))
  print("Delete link data not there:",linkedList.delete_link(20),"\n")


  # Test method copy_list()
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_first(i)
  print("before copied:",linkedList)
  print("copied:",linkedList.copy_list()) # reverse sorted list will be seen 

  # Test method reverse_list()
  linkedList = LinkedList ()
  for i in range (10):
    linkedList.insert_first(i)
  print("unreversed:",linkedList)
  print("reversed:",linkedList.reverse_list()) # expect to see actually sorted list 

  # Test method sort_list()
  for i in range (10):
    linkedList.insert_first(i)
  print("unsorted list:",linkedList)
  print("Sort list:",linkedList.sort_list())


  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  for i in range (11):      # sorted in descending order , returns false 
    linkedList.insert_first(i)
  print("Is sorted:",linkedList.is_sorted(),"\n")

  linkedList = LinkedList ()
  for i in range (11): 
    linkedList.insert_last(i)
  print("Is sorted:",linkedList.is_sorted(),"\n")


  # Test method is_empty()
  linkedList = LinkedList () 
  print("empty?",linkedList.is_empty(),"\n")

  # Test method merge_list()
  linkedList = LinkedList ()
  for i in range (11):
      linkedList.insert_first(i)

  linkedMergeList = LinkedList() 
  for i in range (11,21):      
    linkedMergeList.insert_first(i)
  print("Merged List:",linkedList.merge_list(linkedMergeList),"\n") # prints new list that creates a combined list 

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  linkedList1 = LinkedList ()
  for i in range (10):
    linkedList1.insert_last(i)

  linkedList2 = LinkedList ()
  for i in range (10):
    linkedList2.insert_last(i)
  
  b = [1,4,6,10,5,9]
  linkedList3 = LinkedList ()
  for i in b:
    linkedList3.insert_last(i)

  print("is equal?", linkedList1.is_equal(linkedList2))
  print("is equal?", linkedList2.is_equal(linkedList3),"\n") # the thing in front of the dot is self 
 

  # Test remove_duplicates()
  linkedList = LinkedList ()
  a = [1,2,2,4,2,7,8,8,9,10,11,11]
  for i in a:
    linkedList.insert_last(i)
  print("Removed duplicates:",linkedList.remove_duplicates(),"\n")


if __name__ == "__main__":
  main()