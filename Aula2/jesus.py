import re

f = open('text.txt')
res = set()

for line in f:
 campos = re.split(r'::',line)
 titulo = campos[2]
 jesus = re.search(r'Jesus',titulo)
 
 if jesus:
  res.add(titulo)


print(res)
size = len(res)
print('size: <<<<<<<<<<<<<<<<<<<<<<<<<<<<',size)


f.close()
