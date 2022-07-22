import re

f = open('emd.csv')

for line in f:
 m = re.search(r'^(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+)$',line)
 if(m):
  primeiro = m.group(4)
  ultimo = m.group(5)
  print(f'primeiro: {primeiro}; ultimo: {ultimo}')

 #campos = re.split(r',',line)
 #primeiro = campos[3]

f.close()
