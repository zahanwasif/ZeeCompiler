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
        print(p[1])
        run(p[1])
    except:
        pass

def p_statements_mul(p):
    '''
    statements  : statements SEMIC statements
                | statements
    '''
    if len(p) == 4:
        p[0] = (p[1] , p[3])
    else :
        p[0] = p[1]

def p_statements(p):
    '''
    statements  : statement SEMIC statement
                | statement
    '''
    if len(p) == 4:
        p[0] = (p[1] , p[3])
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

def p_statement_declare(p):
    '''
    statement : DECLARE ID EQUALS expr
    '''
    p[0] = ('declare', p[2] , p[4], 'expr')

def p_statement_declare_id(p):
    '''
    statement : DECLARE ID EQUALS ID
    '''
    p[0] = ('declare', p[2] , p[4], 'ID')

def p_statement_declare_only(p):
    '''
    statement : DECLARE ID
    '''
    p[0] = ('declare-only' , p[2])

def p_statement_print(p):
    '''
    statement : PRINT LPARENTHESIS ID RPARENTHESIS
    '''
    p[0] = ('print' , p[3] , 'ID')

def p_statement_print_expr(p):
    '''
    statement : PRINT LPARENTHESIS expr RPARENTHESIS
    '''
    p[0] = ('print' , p[3] , 'expr')



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
    statement : DO LCURLY statements RCURLY WHILE LPARENTHESIS expr RPARENTHESIS
    '''
    p[0] = ('loop' , p[3], p[7])


def p_list(p):
    '''
    statement : LIST ID
    '''
    p[0] = ('list' , p[2])

def p_push(p):
    '''
    statement : ID DOT PUSH LPARENTHESIS expr RPARENTHESIS
    '''
    p[0] = ('push' , p[1] , p[5] , 'expr')

def p_push_var(p):
    '''
    statement : ID DOT PUSH LPARENTHESIS ID RPARENTHESIS
    '''
    p[0] = ('push' , p[1] , p[5] , 'var')

def p_pop(p):
    '''
    statement : ID DOT POP LPARENTHESIS RPARENTHESIS
    '''
    p[0] = ('pop' , p[1])

def p_pop_var(p):
    '''
    statement : ID DOT POP LPARENTHESIS expr RPARENTHESIS
    '''
    p[0] = ('pop' , p[1] , p[5])

def p_error(p):
    print("SYNTAX ERROR")
    parser.restart()

dic = {}

def run(p):
    if  type(p) == tuple:
        if p[0] == 'ass':
            if p[2] not in dic:
                print("'%s' is not declared yet" % p[2])
                raise Exception
            elif p[1] not in dic:
                print("'%s' is not declared yet" % p[1])
                raise Exception
            else:
                dic[p[1]] = dic[p[2]]
        elif p[0] == '=':
            if p[1] in dic:
                dic[p[1]] = run(p[2])
            else:
                print("'%s' is not declared yet" % p[1])
        elif p[0] == 'declare':
            if p[1] in dic:
                print("You cannot declare agian")
                raise Exception
            else:
                if p[3] == 'expr':
                    dic[p[1]] = p[2]
                else:
                    if p[2] not in dic:
                        print("'%s' is not declared yet" % p[2])
                    else:
                        dic[p[1]] = dic[p[2]]
        elif p[0] == 'declare-only':
            if p[1] in dic:
                print("You cannot declare agian")
                raise Exception
            else:
                dic[p[1]] = None
        elif p[0] == 'print':
            if p[2] == 'expr':
                print(run(p[1]))
            else:
                y = p[1]
                if y in dic:
                    print(dic[y])
                else:
                    print("'%s' is not declared yet" % p[1])
                    raise Exception
        elif p[0] == 'list':
            if p[1] in dic:
                print("'%s' is already declared" % p[1])
            else:
                dic[p[1]] = list([])
        elif p[0] == 'push':
            if p[1] not in dic:
                print("'%s' is not declared yet" % p[1])
                raise Exception
            elif type(dic[p[1]]) is not list:
                print("'%s' is not declared as a list" % p[1])
                raise Exception
            else:
                if p[3] == 'expr':
                    dic[p[1]].append(p[2])
                else:
                    dic[p[1]].append(dic[p[2]])
        elif p[0] == 'pop':
            if p[1] not in dic:
                print("'%s' is not declared yet" % p[1])
                raise Exception
            elif type(dic[p[1]]) is not list:
                print("'%s' is not declared as a list" % p[1])
                raise Exception
            else:
                if len(p) == 3:
                    if len(dic[p[1]]) > int(p[2]):
                        dic[p[1]].pop(p[2])
                    else:
                        print("The index is out of range")
                        raise Exception
                else:
                    dic[p[1]].pop(len(dic[p[1]])-1)
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
            run(p[1])
            while(run(p[2])):
                run(p[1])
        else:
            for x in p:
                run(x)
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

