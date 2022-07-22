# -- Problema: Alien username
import re 

f = open("usernames.txt", "r")

print("««« Search »»»")

for linha in f:
  print(linha)
  #y = re.search(r'(_|.)([0-9]+[A-Za-z]{3,})(\.|_)', linha)
  y = re.search(r'^(_|\.)([0-9]+[A-Za-z]{3,})([.*_]{0,1})',linha)
  if y:
    print("----------inic match------------------")
    #print(y)
    print(y.string)
    print(y.span())
    print(y.groups())
    print(y.group())
    print("Válido")
    print("-----------fim match-------------------")

print("««« Search »»»")
