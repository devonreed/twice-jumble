import time
start = int(round(time.time() * 1000))

# permute() takes a list of letters and a prefix and
# returns all permutations of those letters with the
# prefix appended to the head
def permute(letters, prefix):
  permutations = list()
  for idx, letter in enumerate(letters):
    permutations.append(prefix+letter)
    newletters = list(letters)
    del newletters[idx]
    permutations += permute(newletters, prefix+letter)
  return permutations

# prompt for user input
word = raw_input('Jumble Me! (enter a word): ')
letters = list(word)

# load our dictionary
f = open('2of12.txt', 'r')
possibilities = list()  

# get all permutations of the user's input
allpermutations = permute(letters, '')

# discard duplicates in our permutation list
for idx, p in enumerate(allpermutations):
  allpermutations[idx] = ''.join(sorted(p))
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
