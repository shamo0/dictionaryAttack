import hashlib,string,sys,random

def usage():
  print('Must run with four arguments, one for the file from which to read')
  print('passwords and counts, one for the number of elements in the table,')
  print('one with the filename for the hashed table, and one for the filename')
  print('for the plaintext solution.')
  print('Ex: python3 pwPageGenerator.py shortrockyouwithcount.txt 5000 outHashes.txt outAnswers.txt')

numChoices=0
outFile=''
outAns=''
inFile=''
if len(sys.argv)<5:
  usage()
  exit()
try:
  inFile=sys.argv[1]
  numChoices=int(sys.argv[2])
  outFile=sys.argv[3]
  outAns=sys.argv[4]
except:
  usage()
  exit()
exclude = set(string.punctuation)
usernames=set()
with open('american-english','r') as uns:
  for word in uns:
    un=''.join(ch for ch in word.rstrip() if ch not in exclude)
    usernames.add(un.lower())
passwords=[]
with open(inFile,'r') as pws:
  for line in pws:
    lineArr = line.rstrip().split()
    if len(lineArr)>1:
      for i in range(int(lineArr[0])):
        passwords.append(' '.join(lineArr[1:]))
usernames=random.sample(usernames,numChoices)
with open(outFile,'w') as hashes, open(outAns,'w') as answers:
  for un in usernames:
    m=hashlib.md5()
    pw=random.choice(passwords)
    answers.write(un+'\t'+pw+'\n')
    pw=pw.encode()
    m.update(pw)
    hashes.write(un+'\t'+m.hexdigest()+'\n')
