import sys

flist = []
fname = sys.argv[1]
f = open(fname, 'r')
for i in f:
    tokens = i.strip()
    if len(tokens) > 0:
        flist.append(int(tokens))
f.close()

o = open('%s.yml'%fname.split('.')[0], 'w')
for i in flist:
    f = open('items/%04d.txt'%i, 'r')
    for j in f:
        o.write(j)
    f.close()
    o.write('\n')
o.close()
