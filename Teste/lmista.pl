import ply.lex as lex

tokens = [
 'ID',
 'NUM',
 'PE',
 'PD',
 'VIRG'
]

t_ID = r'\w+'
t_PE = r'\('
t_PD = r'\)'
t_VIRG = r','

def t_NUM(t):
 r'\d+'
 t.value = int(t.value)
 return t

t_ignore = '\n\t'

def t_error(t):
 print('Illegal character: ' + t.value[0])

lexer = lex.lex()

import sys

for line in sys.stdin:
 lexer.input(line)
 for tok in lexer:
  print(tok)


import ply.yacc as yacc

def p_grammar(p):
  """
  lista_mista : PE elementos PD

  elementos : elemento
   			| elemento VIRG elementos

  elemento : ID
  			| NUM
  """
  pass

def p_error(p):
 print('syntax error!')

parser = yacc.yacc()

  