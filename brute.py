#!/usr/bin/python3
from datetime import datetime
from bst import *

import sys

def usage():
  print('This program is to be run with two arguments, and an optional third')
  print('argument.  The first is the filename of your precomputed hash table, such as')
  print('hashedRockyou.txt or shortHashedRockyou.txt.  The second is the file you are')
  print('trying to crack, which was likely created by pwPageGenerator.py, and')
  print('contains usernames and the hashes of passwords.  If you include a third')
  print('argument, it should be the filename of a file that contains common passwords')
  print('and their frequencies, such as rockyouwithcount.txt.')
  print('EXAMPLE:')
  print('python3 brute.py hashRockyou.txt outTable.txt rockyouwithcount.txt')
  print('OR')
  print('python3 brute.py hashRockyou.txt outTable.txt')

if len(sys.argv) != 3 and len(sys.argv) != 4:
  usage()
  exit()
computedHashes=[]
table=[]
counts=[]
try:
  with open(sys.argv[1],'r') as f:
    computedHashes = f.read().splitlines()
  with open(sys.argv[2],'r') as f:
    table = f.read().splitlines()
  if len(sys.argv)==4:
    with open(sys.argv[3],'r') as f:
      counts = f.read().splitlines()
except:
  usage()
  exit()

answerStrings=[]

'''
At this point, the list computedHashes contains every line of our precomputed
hashes, the list table contains every line of our username-hash file, and (if
you included this argument) the list counts contains the number of times each
password appears.  The rest of your code goes between the declaration of the
variables "start" and "stop."  Rather than printing your solution, append what
you want to print into a list "answerStrings," for display after the clock has
stopped.  If you want to change answerStrings to something other than a list,
that's fine, as long as there is nothing happening after stop other than
printing the contents of answerStrings
'''
start=datetime.now()
#---------------------------------------------------------
#Using a built in map
# dictTable = {}
# dictHashpass = {}

# for pair in table:
#     splitPair=pair.split('\t')
#     dictTable[splitPair[1]] =splitPair[0]
#
# for pair in computedHashes:
#     splitPair=pair.split(" ")
#     dictHashpass[splitPair[0]] = splitPair[1]
# for key in dictTable:
#     if key in dictHashpass:
#         answerStrings.append(str(dictTable[key])+" "+key)

#-------------------------------------------------------------
#----------------BST-MAP--------------------------------------
class Node:
    def __init__(self, data) :
        '''Initialize Node with data.'''
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) :
        '''Return string representation of data.'''
        return str(self.data)

class KVPair:
    def __init__(self, key, value) :
        # print("test")
        self.key   = key
        self.value = value

    def __lt__(self, other) :
        if self.key < other.key:
            return True
        return False

    def __le__(self, other) :
        if self.key <= other.key:
            return True
        return False

    def __gt__(self, other) :
        if self.key > other.key:
            return True
        return False

    def __ge__(self, other) :
        if self.key >= other.key:
            return True
        return False

    def __eq__(self, other) :
        if self.key == other.key:
            return True
        return False

    def __ne__(self, other) :
        if self.key != other.key:
            return True
        return False

class TreeSet:
    def __init__(self):
        self.__root = None

    def insert(self,key):
        self.__root = self.__insert(self.__root,key)

    def __insert(self,refNode,key):
        if (refNode==None): #Base Case:empty spot
            return key
        if (refNode.data.key == key.data.key): #Base Case: Already in BST
            return refNode
        if (key.data.key<refNode.data.key):
            refNode.left = self.__insert(refNode.left,key)
        else:
            refNode.right = self.__insert(refNode.right,key)
        return refNode

    def __contains__(self,key):
        return self.__contains(self.__root,key)

    def __contains(self,refNode,key):
        if (refNode==None): #BASE CASE: EMPTY SPOT
            return None
        elif (refNode.data.key == key):
            return True
        if (key<refNode.data.key):
            return self.__contains(refNode.left,key)
        elif (key>refNode.data.key):
            return self.__contains(refNode.right,key)
        else:
            return False

BinTree = TreeSet()
for pair in computedHashes:
    # print(pair)
    splitPair=pair.split(" ")
    pairKV = KVPair(splitPair[0],splitPair[1])
    # print(pairKV)
    nodeToInsert = Node(pairKV)
    # print(nodeToInsert)
    BinTree.insert(nodeToInsert)
#
for pair in table:
    splitPair=pair.split('\t')
    if (splitPair[1] in BinTree):
        answerStrings.append(splitPair[1]+" "+splitPair[0])




#------------------------------------------------------------
stop=datetime.now()
for answers in answerStrings:
  print(answers)
print("Runtime:",stop-start)

