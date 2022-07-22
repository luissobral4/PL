import re

f = open('emd.csv')
next(f)

d = {'2020' : 0}

for line in f:
 campos = re.split(r',',line)
 genero = campos[6]
 data = campos[2]

 if genero == 'F':
  ano = re.split(r'-',data)[0]
  if ano in d.keys():
   d[ano] += 1
  else:
   d[ano] = 1

d = dict(sorted(d.items(), key=lambda p: p[0], reverse = true)
print(d)

f.close()
