import re

f = open('emd.csv')
next(f)

d = {}
d['F'] = 0
d['M'] = 0
#d = {'F' : 0,'F' : 0}

for line in f:
 campos = re.split(r',',line)
 genero = campos[6]
 d[genero]+=1

print('Feminino:', d['F']) 
print('Masculino:',d['M'])


f.close()
