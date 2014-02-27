def permute(letters, prefix):
  permutations = list()
  for idx, letter in enumerate(letters):
    permutations.append(''.join(sorted(prefix+letter)))
    newletters = list(letters)
    del newletters[idx]
    permutations += permute(newletters, prefix+letter)
  return permutations

word = raw_input('Jumble Me! (enter a word): ')
letters = list(word)
f = open('2of12.txt', 'r')
possibilities = list()  
allpermutations = permute(letters, '')
allpermutations = list(set(allpermutations))

keyeddict = {}
for dictword in f:
  dictword = dictword.strip()
  index = ''.join(sorted(dictword));
  if index not in keyeddict:
    keyeddict[index] = list()
  keyeddict[index].append(dictword)
  
for permutation in allpermutations:
  index = ''.join(sorted(permutation))
  if index in keyeddict:
      possibilities += keyeddict[index]
print possibilities
