#!/usr/bin/python3
from datetime import datetime
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

stop=datetime.now()
for answers in answerStrings:
  print(answers)
print("Runtime:",stop-start)
