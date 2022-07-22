import re

f = open('text.txt')
res = set()

for line in f:
 mp3 = re.search(r'mp3',line)
 
 if mp3:
  campos = re.split(r'::',line)
  res.add(campos[2])

print(res)
f.close()
