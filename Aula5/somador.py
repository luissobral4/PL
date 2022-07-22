import re
import sys

flag = False
soma = 0

for line in sys.stdin:
 if re.search(r'on',line):
  flag = True
  print('Soma ativada!')
 elif re.search(r'off',line):
  flag = False
  print('Soma desativada')
 elif m := re.search(r'\d+',line):
  if flag:
   soma += int(m.group())
 elif re.search(r'=',line):
  print('Soma atual:',soma)
