import re

with open('emd.csv') as f:
 next(f)

 d = []

 for line in f:
  campos = re.split(r',',line)
  modalidade = campos[-5]
  if modalidade == 'Atletismo':
   primeiro = campos[3]
   ultimo = campos[4]
   idade = campos[5]
   nome = primeiro + ' ' + ultimo
   d.append((nome,int(idade)))
 

 d.sort(key=lambda p:(p[1],p[0]))

 print(d)

f.close()
