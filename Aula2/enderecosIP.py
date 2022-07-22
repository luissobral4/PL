import re

f = open("enderecosIP.txt","r")

print("<<<< Search >>>>")

for linha in f:
 print(linha)
 y = re.search(r')
 if y:
  print("este é um endereço IPV4!")
 else:
  
