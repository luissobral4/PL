import re
import sys

flag = False
soma = 0

for line in sys.stdin:
 elementos = re.findall(r'on|off|\d+|+',line)
 print(elementos)
 for e in elementos:
  if e == 'on':
   flag = True
   print('Ativada')
  elif e == 'off':
   flag = False
   print('Desativada')
  elif e == '=':
   print('Soma atual:',soma)
  else:
   if flag:
    soma += int(e)

print('Soma total:',soma)
