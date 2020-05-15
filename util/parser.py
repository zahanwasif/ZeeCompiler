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
    try:
        run(p[1])
    except:
        pass

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
    '''
    p[0] = ('=', p[1] , p[3])

def p_statement_equal_ass(p):
    '''
    statement : ID EQUALS ID
    '''
    p[0] = ('ass', p[1] , p[3])



def p_statement_print(p):
    '''
    statement : PRINT LPARENTHESIS VAR LPARENTHESIS statement RPARENTHESIS RPARENTHESIS
              | PRINT LPARENTHESIS statement RPARENTHESIS
    '''
    if len(p) == 8:
        p[0] = ('printvar' , p[5])
    elif len(p) == 5:
        p[0] = ('print' , p[3])
    else :
        raise Exception



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
    statement : IF expr LCURLY statement RCURLY
              | IF expr LCURLY statement RCURLY ELSE LCURLY statement RCURLY
    '''
    if len(p)==6:
        p[0] = ('ifelse', p[2], p[4])
    else :
        p[0] = ('ifelse', p[2], p[4], p[8])


def p_loop(p):
    '''
    statement : LOOP LPARENTHESIS expr COMMA expr RPARENTHESIS LCURLY statement RCURLY
    '''
    p[0] = ('loop' , p[3], p[5], p[8])


def p_error(p):
    print("SYNTAX ERROR")
    parser.restart()

dic = {}

def run(p):
    if  type(p) == tuple:
        if p[0] == 'ass':
            if p[2] in dic:
                dic[p[1]] = dic[p[2]]
            else:
                print("'%s' is not declared yet" % p[2])
                raise Exception
        if p[0] == '=':
            dic[p[1]] = run(p[2])
        elif p[0] == 'print':
            if p[1] in dic:
                print(dic[p[1]])
            else:
                print(run(p[1]))
        elif p[0] == 'printvar':
            print(p[1])

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
        elif p[0]=='inc':
            if p[1] in dic:
                dic[p[1]] += 1
            else:
                print("'%s' is not declared yet" % p[1])
        elif p[0]=='dec':
            if p[1] in dic:
                dic[p[1]] += 1
            else:
                print("'%s' is not declared yet" % p[1])

        elif p[0] == 'ifelse':
            if len(p) == 3:
                if run(p[1]) :
                    run(p[2])
            else :
                if run(p[1]) :
                    run(p[2])
                else :
                    run(p[3])
        elif p[0] == 'loop':
            while(run(p[1])):
                run(p[3])
                run(p[2])

    elif p in dic:
        return dic[p]
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

