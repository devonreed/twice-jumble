import time
start = int(round(time.time() * 1000))

def permute(letters, prefix):
  permutations = list()
  for x in range(0, len(letters)):
    permutations.append(prefix+letters[x])
    permutations += permute(letters[x+1:len(letters)], prefix+letters[x])
  return permutations

word = raw_input('Jumble Me! (enter a word): ')
letters = list(word)
f = open('2of12.txt', 'r')
possibilities = list()  
allpermutations = permute(sorted(letters), '')
allpermutations = list(set(allpermutations))

keyeddict = {}
for dictword in f:
  dictword = dictword.strip()
  index = ''.join(sorted(dictword));
  if index not in keyeddict:
    keyeddict[index] = list()
  keyeddict[index].append(dictword)
  
for permutation in allpermutations:
  if permutation in keyeddict:
      possibilities += keyeddict[permutation]
print possibilities

end = int(round(time.time() * 1000))
print "Total Time Elapsed: " + str(end-start) + "ms";