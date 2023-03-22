#  File: Reducible.py

#  Description:

#  Student Name: K. Amber Vasquez   

#  Student UT EID: kav835

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/27/2020

#  Date Last Modified: 10/30/2020

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    #calculates, how you run secondary hash function 
    #constant - (whatever hashing) % constant
    return const - (hash_word(s,const)) 


# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    idxHashWord = hash_word(s,len(hash_table))
    step = step_size (s,47)          # can be any prime number, you pick. save it to use again 
    i = 0
    while True:
      idxHashWord = (idxHashWord + (i*step)) % len(hash_table)

      if hash_table[idxHashWord] != "":  #we have a collision
        i+= 1
      else:
        hash_table[idxHashWord] = s #list = [ 0,1,2,3,4,5] #list[0] = 7
        return 
    


# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table): # take a word, check at its index to see if there, until we find or find empty string
    idxHashWord = hash_word(s,len(hash_table))
    step = step_size (s,47)          # can be any prime number, you pick. save it to use again 
    i = 0
    while True:
      idxHashWord = (idxHashWord + (i*step)) % len(hash_table)

      if hash_table[idxHashWord] == "":  #we have a collision
        return False
      elif hash_table[idxHashWord] == s: #list = [ 0,1,2,3,4,5] #list[0] = 7
        return True
      else: 
        i += 1
    
# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):

    if s in ["a","i","o"] or find_word(s,hash_memo):
      return True
    elif not find_word(s,hash_table): 
      return False 
    else: 
      possibleWords = []
      for i in range (len(s)):
        newList = list(s) # s = [l,i,b,r,a,r,y]
        #remove a letter
        newList.pop(i)
        v = "".join(newList)
        possibleWords.append(v)
      for i in possibleWords: 
        if is_reducible(i, hash_table, hash_memo):
          insert_word(i,hash_memo)
          return True
      return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    pass
    
def getTen (reducible_words):
  
  length10Words = [] 
  for word in reducible_words: 
    if len(word) == 10:
      length10Words.append(word)
  return length10Words 
  

def test_case ():

 #feed a string, hash table and hash memo
   # create an empty word_list
  word_list = [] 

  # open the file words.txt
  f = open("words.txt","r")

  # read words from words.txt and append to word_list
  line = f.readline().strip()
  while line != "":
    word_list.append(line)
    line = f.readline().strip()
    
  #print(word_list[1:11])

  # close file words.txt
  f.close()

  # find length of word_list
  lengthWordList = len(word_list) 
  #print("Length of word List:",lengthWordList)

  # determine prime number N that is greater than twice
  # the length of the word_list
  n = 2 * (lengthWordList) + 1
  # until n is prime
  while is_prime(n) == False:
    n += 2 

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  # appends an empty string n amount of times
  for i in range (n):
    hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list: 
    insert_word(word, hash_list)
  
  #print (hash_list[1:5])

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  m = int(0.2 * (lengthWordList) + 1)
  print(m)
  while is_prime(m) == False:
    m += 1
  # populate the hash_memo with M blank strings
  hash_memo = []
  for i in range (m):
    hash_memo.append("")
  

  # create an empty list reducible_words
  reducible_words = []
  print(is_reducible("sprite",hash_list, hash_memo)) 
  print(is_reducible("sprite",hash_list, hash_memo)) 

  


def main():
  # create an empty word_list
  word_list = [] 

  # open the file words.txt
  f = open("words.txt","r")

  # read words from words.txt and append to word_list
  line = f.readline().strip()
  while line != "":
    word_list.append(line)
    line = f.readline().strip()
    
  #print(word_list[1:11])

  # close file words.txt
  f.close()

  # find length of word_list
  lengthWordList = len(word_list) 
  #print("Length of word List:",lengthWordList)

  # determine prime number N that is greater than twice
  # the length of the word_list
  n = 2 * (lengthWordList) + 1
  # until n is prime
  while is_prime(n) == False:
    n += 2 

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  # appends an empty string n amount of times
  for i in range (n):
    hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list: 
    insert_word(word, hash_list)
  
  #print (hash_list[1:5])

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  m = int(0.2 * (lengthWordList) + 1)
  while is_prime(m) == False:
    m += 1
  # populate the hash_memo with M blank strings
  hash_memo = []
  for i in range (m):
    hash_memo.append("")
  

  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list: 
    if is_reducible(word,hash_list,hash_memo):
      #print("Reducible word:",word)
      reducible_words.append(word) 

  # find words of length 10 in reducible_words
  length10Words = getTen(reducible_words) 
  length10Words.sort()

  # print the words of length 10 in alphabetical order
  # one word per line

  for word in length10Words: 
    print(word)

if __name__ == "__main__":
  main()
  #test_case()