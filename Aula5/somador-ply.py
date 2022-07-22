import ply.lex as lex

# ER -> ação

# lista de tokens OBRIGATORIA
tokens = [
   'ON'
   'OFF'
   'EQUAL'
   'NUMBER'
]

flag = False
soma = 0

def t_ON(t):
 r'(?i:on)'
 global flag
 glag = True
 print('Soma ativada!')
 return t

def t_OFF(t):
 r'(?i:off)'
 global flag
 flag = false
 print('Soma desativada!')
 return t

def t_EQUAL(t):
 r'='
 print('Soma Atual:',soma)
 return t

def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 if flag:
  global soma
  soma += t.value
 return t

data = 'on 1 2 3 = off 2 2 =on 2 2 ='

lexer = lex.lex()

lexer.input(data)

while True:
 token = lexer.token()
 if not token:
  break
 print(token)

print('Soma total:',soma)
