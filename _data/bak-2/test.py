f = open('journal-2014-b.yml', 'r')

items = []
item = []

for i in f:
    if i.strip().startswith('- title:'):
        if len(item) > 0:
            items.append(item)
        item = []
        item.append(i)
    else:
        item.append(i)
items.append(item)

f.close()
print(items)
print(len(items))

n0 = 1
for item in items:
    fname = 'items/%04d.txt'%n0
    o = open(fname, 'w')
    for i in item:
        o.write(i)
    o.close()
    n0 += 1
