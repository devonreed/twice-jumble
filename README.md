* Summary

I took a few cracks at this, and went ahead and used Python since it seems to be an important part of Twice's setup.

My first attempt was dumbjumble.py, which runs in O(n!) time.  It creates all possible permutations of the letters in the jumble and checks the dictionary to see if they are in there.

That attempt was painfully slow, so the second attempt fastjumble.py uses the same permutation, but orders the letters in the permutations and then compares them against a keyhash of the dictionary in which the indexes are ordered letters in the words.  This is markedly faster, and would be faster still if the keyed dictionary were the original loaded file, rather than reindexing on every execution of the program.

The final attempt was just a polish of fastjumble.py - fasterjumble.py - which doesn't create every permutation of the letters in the jumble, but instead only the ordered permutations.  The speed difference seems to be negligible in the smaller words, but more significant in larger ones.

* Logs

admins-MacBook-Pro-34:twice-jumble dreed$ python dumbjumble.py 
Jumble Me! (enter a word): python
['h', 'ho', 'hon', 'hop', 'hot', 'hypo', 'n', 'no', 'not', 'nth', 'o', 'oh', 'on', 'opt', 'p', 'phony', 'pony', 'pot', 'python', 't', 'tho', 'thy', 'to', 'ton', 'tony', 'top', 'toy', 'typo', 'y', 'yo', 'yon']
Total Time Elapsed: 13897ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fastjumble.py 
Jumble Me! (enter a word): python
['thy', 'pony', 'o', 'tony', 'hot', 'tho', 'hop', 'nth', 'opt', 'pot', 'top', 'python', 'hypo', 'toy', 'yon', 'not', 'ton', 'phony', 'no', 'on', 'h', 'hon', 'n', 'p', 'typo', 't', 'yo', 'y', 'to', 'ho', 'oh']
Total Time Elapsed: 2494ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fasterjumble.py 
Jumble Me! (enter a word): python
['opt', 'pot', 'top', 'p', 'o', 'thy', 'pony', 'hypo', 'no', 'on', 'tony', 'hot', 'tho', 'hop', 't', 'y', 'python', 'toy', 'ho', 'oh', 'not', 'ton', 'phony', 'to', 'h', 'hon', 'n', 'typo', 'nth', 'yo', 'yon']
Total Time Elapsed: 2962ms

admins-MacBook-Pro-34:twice-jumble dreed$ python dumbjumble.py 
Jumble Me! (enter a word): fashion
['a', 'ah', 'an', 'as', 'ash', 'f', 'fa', 'fain', 'fan', 'fashion', 'fin', 'fish', 'h', 'ha', 'has', 'hi', 'his', 'ho', 'hon', 'i', 'if', 'in', 'info', 'ion', 'is', 'n', 'naif', 'no', 'nosh', 'o', 'oaf', 'oafish', 'of', 'oh', 'on', 's', 'sh', 'shin', 'sin', 'so', 'sofa', 'son']
Total Time Elapsed: 93452ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fastjumble.py 
Jumble Me! (enter a word): fashion
['info', 'fain', 'naif', 'shin', 'fashion', 'fin', 'his', 'son', 'h', 'fish', 'sofa', 'n', 'oafish', 'o', 's', 'so', 'ash', 'has', 'sh', 'hi', 'ho', 'oh', 'sin', 'f', 'nosh', 'fa', 'ah', 'ha', 'is', 'an', 'as', 'ion', 'fan', 'oaf', 'no', 'on', 'if', 'of', 'a', 'in', 'i', 'hon']
Total Time Elapsed: 2186ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fasterjumble.py 
Jumble Me! (enter a word): fashion
['info', 'fain', 'naif', 'shin', 'fashion', 'fin', 'his', 'h', 'son', 'fish', 'sofa', 'n', 'oafish', 'o', 's', 'so', 'ash', 'has', 'sh', 'hi', 'ho', 'oh', 'sin', 'f', 'nosh', 'fa', 'ah', 'ha', 'is', 'an', 'as', 'ion', 'fan', 'oaf', 'no', 'on', 'if', 'of', 'a', 'in', 'i', 'hon']
Total Time Elapsed: 2357ms

admins-MacBook-Pro-34:twice-jumble dreed$ python dumbjumble.py 
Jumble Me! (enter a word): speed
['d', 'deep', 'e', 'ed', 'p', 'pee', 's', 'see', 'seed', 'seep', 'sped', 'speed']
Total Time Elapsed: 27296ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fastjumble.py 
Jumble Me! (enter a word): speed
['seed', 'deep', 'pee', 'seep', 'ed', 'e', 'd', 'speed', 'see', 'p', 's', 'sped']
Total Time Elapsed: 1587ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fasterjumble.py 
Jumble Me! (enter a word): speed
['seed', 'deep', 'pee', 'seep', 'ed', 'e', 'd', 'speed', 'see', 'p', 's', 'sped']
Total Time Elapsed: 1398ms

admins-MacBook-Pro-34:twice-jumble dreed$ python fastjumble.py 
Jumble Me! (enter a word): exercise
['seer', 'sere', 'cries', 'ice', 'rice', 'sec', 'rec', 'rise', 'sire', 'see', 'ere', 'x', 'ex', 're', 'sir', 'sex', 'c', 'six', 'scree', 's', 'xi', 'cerise', 'ire', 'sic', 'r', 'eerie', 'is', 'siree', 'exec', 'excise', 'e', 'i', 'exercise']
Total Time Elapsed: 4763ms
admins-MacBook-Pro-34:twice-jumble dreed$ python fasterjumble.py 
Jumble Me! (enter a word): exercise
['seer', 'sere', 'cries', 'ice', 'rice', 'sec', 'rec', 'rise', 'sire', 'see', 'ere', 'x', 're', 'sir', 'sex', 'ex', 'c', 'six', 'scree', 's', 'exec', 'xi', 'cerise', 'ire', 'sic', 'r', 'eerie', 'is', 'siree', 'excise', 'e', 'i', 'exercise']
Total Time Elapsed: 2532ms
