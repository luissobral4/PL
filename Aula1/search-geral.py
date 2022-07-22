import re

def busca(ER):
  fraseFonte = input(">> ")
  while fraseFonte != "":
    y = re.search(ER, fraseFonte)
    if(y): 
      print("Em \'", y.string, "\' foi encontrado: ", y.group())   
    else:
      print("Não encontrado")
    fraseFonte = input(">> ")

# 1.
def ex1(): 
 print("Linhas que contém algures a palavra 'padrão'")
 busca(r'(?i:(P|p)adrão)')
#[Pp]

# 2.
def ex2(): 
 print("Linhas que começam por 'PRH' ou 'JCR' ")
 busca(r'^(PRH|JCR)$')
#'(PRH|JCR)$' no fim da frase

# 3.
def ex3(): 
 print("Linhas que começam por um Número")
 busca(r'^[1234567890]+') # '*' cada carater pode aparecer 0 ou varias vezes
 #[0-9]

# 4. 
def ex4():
 print("Linhas que terminam com 'PMoura'")
 busca(r'PMoura$')

# 5. 
def ex5():
 print("Linhas que terminam com: uma Letra (maíscula ou minúscula), ou com um ponto de interrogação, ou ponto final")
 busca(r'[A-Za-z.?]$')
#'(?i:[a-z|\.|\?]$'

# 6. 
def ex6():
 print("Linhas que só contém digitos, hífens ou pontos")
 busca(r'^([A-Za-Z.\-]+)$')

# 7.
def ex7(): 
 print("Linhas que começam por um ou mais Separadores de palavras (white spaces)")
 busca(r'^[ \t]+')

# 8.
def ex8():
 print("Linhas que contém um número de telefone português (9 digitos)")
 busca(r'9[0-9]{8}')

##8a. permita que comece pelo indicativo do país
def ex8a():
 print("Linhas que contém um número de telefone português (9 digitos)")
 busca(r'+3529[0-9]{8}')

# 9. 
def ex9():
 print("Linhas que contém uma STRING não nula entre aspas")
 #busca(r' ".+" ') tenta apanhar o maximo de carateres
 #busca(r' ".+?" ') apanha o 1ª
 busca(r'"[^"]+"')

## 9a. repita o exercício anterior permitindo Strings vazias
def ex9a():
 print("Linhas que contém uma STRING não nula entre aspas")
 busca(r'"([^"]+)?"')

## 9.b repita o exercício anterior escrevendo apenas o texto entre aspas

# 10. A phone number. This is three digits followed by a dash followed by four digits. 
# 11. This time your phone number should not have an area code - only the three digit, dash, four digit local phone number. (You can assume that your phone number is preceded by a whitespace character.)
# 12. Last, allow your phone number to be seven consecutive digits as well as the three digit dash four digit type.
