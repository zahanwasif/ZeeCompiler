# Add the Libraries required

import ply.lex as lex
import numpy as np
import sys

# Creating tokens for the lexer

tokens = [
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'AND',
    'OR',
    'LCURLY',
    'RCURLY',
    'LPARENTHESIS',
    'RPARENTHESIS',
    'INT',
    'FLOAT',
    'STRING',
    'ID',
    'LSQUARE',
    'RSQUARE',
    'EQUALS',
    'INCREMENT',
    'DECREMENT',
    'GREATER',
    'SMALLER',
    'GEQUAL',
    'SEQUAL',
    'CHAR',
    'BOOL'

]

reserved = {
    'if' : "IF",
    'else' : "ELSE",
    'elseif' : "ELSEIF",
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'jump': 'JUMP',
    # 'TRUE' : 'TRUE',
    # 'FALSE' : 'FALSE',
    'break' : 'BREAK'
}

# Adding reserved words into the token list
tokens = tokens + list(reserved.values())

states = (
    ('COM','exclusive'),
)

def t_COM(t):
    r'\/\*'
    t.lexer.begin('COM')

def t_COM_end(t):
    r'\*\/'
    t.lexer.begin('INITIAL')

def t_COM_error(t):
    t.lexer.skip(1)

t_COM_ignore = r'.'

# Defining rules to te programming language
t_ADD = r'\+'
t_SUBTRACT = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/' 
t_AND = r'\&\&\&'
t_OR = r'\|\|\|'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPARENTHESIS = r'\(' 
t_RPARENTHESIS = r'\)'


def t_GEQUAL(t):
    r'\>[ ]*\='
    t.value = '>='
    return t


def t_SEQUAL(t):
    r'\<[ ]*\='
    t.value = '<='
    return t


t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_EQUALS = r'\='
t_GREATER = r'\>'
t_SMALLER = r'\<'

def t_BOOL(t):
    r'TRUE|FALSE'
    if (t.value == 'TRUE'):
        t.value = True
    else: t.value = False
    return t

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t 

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'(\'.{0,1}\')'
    t.value=t.value[1:-1]
    return t

def t_STRING(t):
    r'(\".*\")|(\'.*\')'
    t.value=t.value[1:-1]
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
    return t

def t_comment(t):
    r'\/\/.*\n'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal Character used : '%s'" % t.value[0])
    t.lexer.skip(1)
    pass


lexer = lex.lex()
data = input()
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

