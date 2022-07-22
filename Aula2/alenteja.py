import re

f = open('text.txt')
res = set()

for line in f:
 campos = re.split(r'::',line)
 if campos[0] == 'Alentejo':
  res.add(campos[2])

print(res)
f.close()
