#  File: Radix.py
#  Description: modify the Radix Sort algorithm 
# so that it sorts strings that have a mix of lower case letters and digits
#  Student Name: Amber 
#  Date Created: 10/30/2020
#  Date Last Modified: 11/2/2020

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  def __str__ (self):
    #convert a list into a string 
    return str(self.queue) # returns the string version of this list 
    

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    # a = word list 
    queueList = []
    for i in range(37):
      queueList += [Queue()] #creates a new instance of the Queue, is like appending


   
    
    dictionary = {"_":0, "0":1, "1":2,"2":3,"3":4,"4":5,"5":6,"6":7,"7":8,"8":9,"9":10,"a":11,
                  "b":12,"c":13,"d":14,"e":15,"f":16,"g":17,"h":18,"i":19,"j":20,"k":21,"l":22,
                  "m":23,"n":24,"o":25,"p":26,"q":27,"r":28,"s":29,"t":30,"u":31,"v":32,"w":33,
                  "x":34,"y":35,"z":36}
    

    l = [] # has the length of every string in list 
    for i in a: 
      l.append(len(i))
    stringSize = max(l) # also max *pass* value, stringSize variable is the maximum string size from the list
                        # that all other strings need to match with 

    newAList = Queue()  # use for all our calculations, its our fixed strings
    # create a dictionary with the original length, and a dict with key 
    # keys coming from newAlist
    for i in a:
      if len(i) != stringSize: 
        # you can concatinate strings 
        pad = stringSize - len(i) # number of zeros I need to pad onto string to mak eit equal tostringSize
        # concatinate "000" + ""
        newAList.enqueue(i + "_" * pad)  # fixed string)
      else:
        newAList.enqueue(i) # this list is the same as original list, but with the padding of zeros. Not sorted. 

        
    # start sorting new list 
    for i in range(stringSize): # this will be the max pass value, max string size
      for j in range(newAList.size()):   # goes through every word in the list newAList, gets us size of new a list used as a counter, we dont have to access j 
        # the pass
        # for every word in there, for every pass, we have to dequeue all the words 
        word = newAList.dequeue() # returns the next word in the queue
        character = word[-1 - i] # feeds into dictionary, feeds out an index to access in queue 
        queueList[dictionary[character]].enqueue(word)        # this fills up our queue with the first pass
                                                              
      for i in queueList: # i will = every queue in queue list
        # DQ everything back t newAlist
        # call size on i to check for size of i 
        for j in range(i.size()):
          newAList.enqueue(i.dequeue()) # every item in i will be DQ back into new A list

      # get a list of all the strings
      # take out all the underscores 
      '''finalList = newAList.queue # for everything in finalAList, take each word and take out underscores
      for i in range(len(finalList)): # i is index of each word in the list "finalAList"
        #finalAList[i] is each word in the list
        # str.replace will replace any undescore, if your 2nd argument is nothing, takes underscore out
        finalList[i] = finalList[i].replace('_','')
      return finalList
      '''


    
    # create a list to hold them in the correct order as you define in the dictionary 
    # full of the queue objects
    return newAList.queue # the list inside the Queue object 
  # helper function to append correct amount of leading underscores for words that get fed into radix sort 


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  #print (sorted_list)

  finalList = sorted_list # for everything in finalAList, take each word and take out underscores
  for i in range(len(finalList)): # i is index of each word in the list "finalAList"
        #finalAList[i] is each word in the list
        # str.replace will replace any undescore, if your 2nd argument is nothing, takes underscore out
    finalList[i] = finalList[i].replace('_','')
  print(finalList)

if __name__ == "__main__":
  main()

