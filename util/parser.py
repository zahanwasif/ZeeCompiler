import numpy as np
import ply.lex as lex
import ply.yacc as yacc
from lexer import tokens
import lexer


precedence=(
    ('left','AND','OR'),
    ('left','GREATER','SMALLER','GEQUAL','SEQUAL'),
    ('left','ADD','SUBTRACT'),
    ('left','MULTIPLY','DIVIDE','MODULUS'),
)

start = "start"

def p_start(p):
    '''
    start  : statements
           | empty
    '''
    run(p[1])

def p_statements(p):
    '''
    statements  : statements statement
                | statement
    '''
    if len(p) == 3:
        p[0] = (p[1] , p[2])
    else :
        p[0] = p[1]   

def p_empty(p):
    '''
    empty :
    '''
    pass


def p_statement_equal(p):
    '''
    statement : ID EQUALS expr
              | ID EQUALS ID
    '''
    p[0] = ('=', p[1] , p[3])


def p_statement_print(p):
    '''
    statement : PRINT LPARENTHESIS expr RPARENTHESIS
    '''
    p[0] = ('print' , p[3])

def p_statement(p):
    '''
    statement : expr
    '''
    p[0] = p[1]


def p_expr_divide(p):
    'expr : expr DIVIDE expr'
    p[0] = ('/',p[1],p[3])

def p_expr_multiply(p):
    'expr : expr MULTIPLY expr'
    p[0] = ('*',p[1],p[3])

def p_expr_add(p):
    'expr : expr ADD expr'
    p[0] = ('+',p[1],p[3])

def p_expr_subtract(p):
    'expr : expr SUBTRACT expr'
    p[0] = ('-',p[1],p[3])


def p_binary_opr(p):
    '''
    expr : expr MODULUS expr
         | expr EEQUALS expr
         | expr GREATER expr
         | expr SMALLER expr
         | expr AND expr
         | expr OR expr
         | expr NOTEQUALS expr
         | expr GEQUAL expr
         | expr SEQUAL expr
    '''
    p[0]=( p[2] , p[1] , p[3] )

def p_unary_opr(p):
    '''
    expr : expr INCREMENT
         | expr DECREMENT

    '''
    p[0]=(p[2],p[1])

def p_expr_ID(p):
    '''
    expr : ID
    '''
    p[0] = p[1]

def p_num(p):
    '''
    expr : INT
           | FLOAT
           | STRING
           | CHAR
           | BOOL
    '''
    p[0] = p[1]


def p_conditionals(p):
    '''
    statement : ifstatement
              | ifstatement elsestatement
    '''
    if len(p)==2:
        p[0]=p[1]
    else :
        p[0] = (p[1], p[2])

def p_ifstatement(p):
    '''
    ifstatement : IF expr LCURLY statement RCURLY
    '''
    p[0]=('if' , p[2] , p[4])

def p_elsestatement(p):
    '''
    elsestatement : ELSE LCURLY statement RCURLY
    '''
    p[0]=('else' , p[3])


def p_loop(p):
    '''
    expr : LOOP LPARENTHESIS expr RPARENTHESIS LCURLY statements RCURLY
    '''
    p[0] = ('loop' , p[3], p[6])


def p_error(p):
    print("SYNTAX ERROR ON LINE NNUMER : ",p.lineno)

dic = {}

def run(p):
    if  type(p) == tuple:
        if p[0] == '=':
            dic[p[1]] = run(p[2])

        elif p[0] == 'print':
            print(run(p[1]))

        elif p[0]=='+':
            return run(p[1]) + run(p[2])

        elif p[0]=='-':
            return run(p[1]) - run(p[2])

        elif p[0] == '*':
            return run(p[1]) * run(p[2])

        elif p[0] == '/':
            return run(p[1]) / run(p[2])

        elif p[0]=='%':
            return run(p[1]) % run(p[2])
        elif p[0]=='&&':
            return run(p[1]) & run(p[2])
        elif p[0]=='||':
            return run(p[1]) | run(p[2])
        elif p[0]=='==':
            return run(p[1]) == run(p[2])
        elif p[0]=='>':
            return run(p[1]) > run(p[2])
        elif p[0]=='<':
            return run(p[1]) < run(p[2])
        elif p[0]=='!=':
            return run(p[1]) != run(p[2])
        elif p[0]=='>=':
            return run(p[1]) >= run(p[2])
        elif p[0]=='<=':
            return run(p[1]) <= run(p[2])
    else:
        return p
        

lex.lex(module = lexer)
parser = yacc.yacc()

while True:
    try:
        data = input("ZEE >>> ")
    except EOFError:
        break
    if data == "":
        continue
    parser.parse(data)
