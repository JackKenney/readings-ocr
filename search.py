import subprocess as sp
import sys
import pprint
import operator

# uses local search.sh script.
print('Looking for:', sys.argv[1:])
# Identify documents containing args
sources = []
for i in range(1, len(sys.argv)):
    try:
        lst = str(sp.check_output(['sh', 'search.sh', sys.argv[i]]))
        lst = lst[2:len(lst)-3].split('\\n')
        sources.extend(lst)
    except sp.CalledProcessError:
        print(sys.argv[i], 'not found.')
# Create sorted printout of documents by number of matching args
# TODO: If the number of args matched is less than the number of args total,
# describe which args matched.
lookup = {}  # count list
for i in sources:
    if i not in lookup:
        lookup[i] = 1
    else:
        lookup[i] += 1

lookup = sorted(lookup.items(), key=operator.itemgetter(1), reverse=True)
pprint.pprint(lookup)
