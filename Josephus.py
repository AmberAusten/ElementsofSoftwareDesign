#  File: Josephus.py
#  Description: uses circular linked lists
#  Student Name: Amber 
#  Date Created: 11/7/2020
#  Date Last Modified: 11/8/2020
import sys

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next 

class CircularList(object):
  # Constructor
  def __init__ ( self ): 
    self.last = None # if we have an empty list, then we have nothing 

  # Insert an element (value) in the list
  def insert ( self, data):
    # insert after last link you put in 
    if self.last == None: # if list is empty
        new_link = Link(data)
        self.last = new_link 
        self.last.next = new_link 
    else:   
        new_link = Link(data) # new link is an address 
        new_link.next = self.last.next # points to the first value in the list 
        #reset self.last next attribute
        # self.last a vairable we have that holds the link, a keyword for last link in the lsit 
        self.last.next = new_link #resets self.last next attribute
        self.last = new_link 


  # Find the link with the given data (value)
  def find ( self, data ):
    if self.last == None: 
        return None

    currentLink = self.last # points to the first one 
    if data == currentLink.data: 
      return currentLink
    currentLink = currentLink.next 
    while currentLink != self.last: 
      if data == currentLink.data: 
        return currentLink
      currentLink = currentLink.next
     
    return None

  # Delete a link with a given data (value)
  def delete ( self, data ):
    if self.last == None: # if list is empty
        return None
    # keep track of link pinter 
    previousLink = self.last 
    # update previous link after we update current link 
    currentLink = self.last.next 
    
    # if the link is the last link in the list 
    if currentLink == previousLink: # then we know we onlyhave this one link 
      self.last == None 
      currentLink.next = None # so our main while loop will exit 
      return currentLink
    # if we need to delete the current self.last, if we need to delete the link that self.last points to, redirect self . last somewhere else


    if currentLink.data == data: 
        previousLink.next = currentLink.next
        return currentLink 
    currentLink = currentLink.next 
    previousLink = previousLink.next

    while currentLink != self.last.next: # once current link equals the data we want to delete 
      # rearrange the arrows so none point at current anymore 
      if currentLink.data == data: 
        if currentLink == self.last:
          self.last = currentLink.next
        previousLink.next = currentLink.next
        return currentLink 
      currentLink = currentLink.next 
      previousLink = previousLink.next
    
    return None 

    # edge cases - for this function 
    # if the link is last link , we have to reset self . last to equal someting else 
    # if its empty 
    # if delete the only link, list only has one link, set self.last to == none 

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ): #start is a link 
    # uses find and the delete methods 
    # counts up from a start n amount of times, deletes the one after
    for i in range(n-1): 
      start = start.next
     # delete start 
    deletedLink = self.delete(start.data) # deletes the link, need to feed in the data not the link 
     # delete returns a link 
     # return the link after the one we deleted 
    return deletedLink.next,deletedLink.data # returns a tuple of those two values 




# in main print deletedLink.data 


# similar to find and deltee, adjust to fit to delete after rules 
  # Return a string representation of a Circular List
  def __str__ ( self ):

    if self.last == None: 
        return None
    
    currentLink = self.last.next # points to the first one 
    # stop when currentLink == None 
    string = ""
    i = 0

    string += str(currentLink.data) + "  "
    i += 1
    currentLink = currentLink.next
    while currentLink != self.last.next: 
      string += str(currentLink.data) + "  "
      i += 1
      currentLink = currentLink.next
      # when i == 10, add \n character 
      if i == 10:
        string += "\n"
        i = 0
    return string

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line) # first soldier we need to delete 

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line) #n

  # your code
  circularList = CircularList()
  
  for i in range(1,num_soldiers +1):
      circularList.insert(i)
  #print(circularList)

  #print("data is there:",circularList.find(35).data)
  #print("Data isn't there:",circularList.find(50))

  #print("delete value:", circularList.delete(5).data)

  # do something one time, then something in a while loop 
  #find our start link, (the data value as our start link)
  firstStart = circularList.find(start_count) 
  t = circularList.delete_after(firstStart,elim_num) # returns a tuple of values 
  print(t[1])
  # enter a while 
  while t[0] != None: 
    t = circularList.delete_after(t[0],elim_num) # returns a tuple of values 
    print(t[1])




if __name__ == "__main__":
  main()
