import ply.lex as lex

tokens = [
  'INT',
  'FLOAT',
  'PLUS',
  'MULT',
  'SUB',
  'DIV',
  'ID'
]

def t_INT(t):
 r'\d+'
 retunr t

def t_FLOAT(t):
 r'\d+\.\d+'
 retunr t
