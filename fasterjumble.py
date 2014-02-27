import time
start = int(round(time.time() * 1000))

# orderspermute() takes a list of letters and a prefix and
# returns all ordered permutations of those letters with the 
# prefix attached
def orderedpermute(letters, prefix):
  permutations = list()
  for x in range(0, len(letters)):
    permutations.append(prefix+letters[x])
    permutations += orderedpermute(letters[x+1:len(letters)], prefix+letters[x])
  return permutations

# prompt for user input
word = raw_input('Jumble Me! (enter a word): ')
letters = list(word)

# load our dictionary
f = open('2of12.txt', 'r')
possibilities = list()  

# get all ordered permutations of the user's input
allpermutations = orderedpermute(sorted(letters), '')
allpermutations = list(set(allpermutations))

# assemble a hashmap where the keys for the words are sorted
# letters in the words
keyeddict = {}
for dictword in f:
  dictword = dictword.strip()
  index = ''.join(sorted(dictword));
  if index not in keyeddict:
    keyeddict[index] = list()
  keyeddict[index].append(dictword)
  
# check and see if the sorted permutations match any keys  
for permutation in allpermutations:
  if permutation in keyeddict:
      possibilities += keyeddict[permutation]
print possibilities

end = int(round(time.time() * 1000))
print "Total Time Elapsed: " + str(end-start) + "ms";