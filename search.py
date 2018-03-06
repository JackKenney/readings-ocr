import subprocess as sp
import sys
import pprint
# uses local search.sh script.
print('Looking for:', sys.argv)
sources = []
for i in range(1, len(sys.argv)):
    try:
        lst = str(sp.check_output(['sh', 'search.sh', sys.argv[i]]))
        lst = lst[2:len(lst)-3].split('\\n')
        sources.extend(lst)
    except sp.CalledProcessError:
        print(sys.argv[i], 'not found.')
lookup = {} # count list
for i in sources:
    if i not in lookup:
        lookup[i] = 1
    else:
        lookup[i] += 1
pprint.pprint(lookup)
