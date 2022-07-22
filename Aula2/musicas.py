import re

f = open('text.txt')
res = {}

for line in f:
 campos = re.split(r'::',line)
 regiao = campos[0]
 if regiao in res:
  res[regiao] += 1
 else:
  res[regiao] = 1

print(res)
f.close()
