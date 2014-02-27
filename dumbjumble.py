import time
start = int(round(time.time() * 1000))

def permute(letters, prefix):
  permutations = list()
  for idx, letter in enumerate(letters):
    permutations.append(prefix+letter)
    newletters = list(letters)
    del newletters[idx]
    permutations += permute(newletters, prefix+letter)
  return permutations

word = raw_input('Jumble Me! (enter a word): ')
letters = list(word)
f = open('2of12.txt', 'r')
possibilities = list()  
allpermutations = permute(letters, '')
for dictword in f:
  dictword = dictword.strip()
  for permutation in allpermutations:
    if permutation == dictword:
      possibilities.append(dictword)
      break
print possibilities

end = int(round(time.time() * 1000))
print "Total Time Elapsed: " + str(end-start) + "ms";