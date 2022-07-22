import re

f = open('emd.csv')
next(f)

clubes = set()
for line in f:
 campos = re.split(r',',line)
 clube = campos[-4]

 clubes.add(clube)

clubes = list(clubes)
clubes.sort()
print(clubes)

f.close()
