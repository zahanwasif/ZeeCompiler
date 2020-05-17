
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startleftANDORleftGREATERSMALLERGEQUALSEQUALleftADDSUBTRACTleftMULTIPLYDIVIDEMODULUSADD AND BOOL CHAR COMMA DECLARE DECREMENT DIVIDE DO DOT EEQUALS ELSE EQUALS FLOAT GEQUAL GREATER ID IF INCREMENT INT LCURLY LIST LOOP LPARENTHESIS MODULUS MULTIPLY NOTEQUALS OR POP PRINT PUSH RCURLY RPARENTHESIS SEMIC SEQUAL SMALLER STRING SUBTRACT VAR WHILE\n    start  : statements\n           | empty\n    \n    statements  : statements SEMIC statements\n                | statements\n    \n    statements  : statement SEMIC statement\n                | statement\n    \n    empty :\n    \n    statement : ID EQUALS expr\n    \n    statement : ID EQUALS ID\n    \n    statement : DECLARE ID EQUALS expr\n    \n    statement : DECLARE ID EQUALS ID\n    \n    statement : DECLARE ID\n    \n    statement : PRINT LPARENTHESIS ID RPARENTHESIS\n    \n    statement : PRINT LPARENTHESIS expr RPARENTHESIS\n    \n    statement : expr\n    expr : expr DIVIDE exprexpr : expr MULTIPLY exprexpr : expr ADD exprexpr : expr SUBTRACT expr\n    expr : expr MODULUS expr\n         | expr EEQUALS expr\n         | expr GREATER expr\n         | expr SMALLER expr\n         | expr AND expr\n         | expr OR expr\n         | expr NOTEQUALS expr\n         | expr GEQUAL expr\n         | expr SEQUAL expr\n    \n    expr : expr INCREMENT\n         | expr DECREMENT\n\n    \n    expr : ID\n    \n    expr : INT\n           | FLOAT\n           | STRING\n           | CHAR\n           | BOOL\n    \n    statement : IF expr LCURLY statement RCURLY\n              | IF expr LCURLY statement RCURLY ELSE LCURLY statement RCURLY\n    \n    statement : DO LCURLY statements RCURLY WHILE LPARENTHESIS expr RPARENTHESIS\n    \n    statement : LIST ID\n    \n    statement : ID DOT PUSH LPARENTHESIS expr RPARENTHESIS\n    \n    statement : ID DOT PUSH LPARENTHESIS ID RPARENTHESIS\n    \n    statement : ID DOT POP LPARENTHESIS RPARENTHESIS\n    \n    statement : ID DOT POP LPARENTHESIS expr RPARENTHESIS\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,12,13,14,15,16,34,35,36,39,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,68,69,70,71,76,78,80,81,82,88,89,],[-7,0,-1,-2,-6,-31,-15,-32,-33,-34,-35,-36,-29,-30,-12,-31,-40,-3,-5,-9,-8,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-11,-10,-13,-14,-43,-37,-42,-41,-44,-39,-38,]),'ID':([0,7,9,11,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[5,36,39,41,5,5,44,39,39,39,39,39,39,39,39,39,39,39,39,39,62,5,68,5,74,39,39,5,]),'DECLARE':([0,17,18,40,64,85,],[7,7,7,7,7,7,]),'PRINT':([0,17,18,40,64,85,],[8,8,8,8,8,8,]),'IF':([0,17,18,40,64,85,],[9,9,9,9,9,9,]),'DO':([0,17,18,40,64,85,],[10,10,10,10,10,10,]),'LIST':([0,17,18,40,64,85,],[11,11,11,11,11,11,]),'INT':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'FLOAT':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'STRING':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'CHAR':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'BOOL':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'SEMIC':([2,4,5,6,12,13,14,15,16,34,35,36,39,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,65,68,69,70,71,76,78,80,81,82,88,89,],[17,18,-31,-15,-32,-33,-34,-35,-36,-29,-30,-12,-31,-40,17,-5,-9,-8,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,17,-11,-10,-13,-14,-43,-37,-42,-41,-44,-39,-38,]),'RCURLY':([4,5,6,12,13,14,15,16,34,35,36,39,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,65,68,69,70,71,72,76,78,80,81,82,87,88,89,],[-6,-31,-15,-32,-33,-34,-35,-36,-29,-30,-12,-31,-40,-3,-5,-9,-8,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,73,-11,-10,-13,-14,78,-43,-37,-42,-41,-44,89,-39,-38,]),'EQUALS':([5,36,],[19,61,]),'DOT':([5,],[20,]),'DIVIDE':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,21,-32,-33,-34,-35,-36,-29,-30,21,-31,-31,21,-16,-17,21,21,-20,21,21,21,21,21,21,21,21,-31,21,-31,21,-31,21,21,21,]),'MULTIPLY':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,22,-32,-33,-34,-35,-36,-29,-30,22,-31,-31,22,-16,-17,22,22,-20,22,22,22,22,22,22,22,22,-31,22,-31,22,-31,22,22,22,]),'ADD':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,23,-32,-33,-34,-35,-36,-29,-30,23,-31,-31,23,-16,-17,-18,-19,-20,23,23,23,23,23,23,23,23,-31,23,-31,23,-31,23,23,23,]),'SUBTRACT':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,24,-32,-33,-34,-35,-36,-29,-30,24,-31,-31,24,-16,-17,-18,-19,-20,24,24,24,24,24,24,24,24,-31,24,-31,24,-31,24,24,24,]),'MODULUS':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,25,-32,-33,-34,-35,-36,-29,-30,25,-31,-31,25,-16,-17,25,25,-20,25,25,25,25,25,25,25,25,-31,25,-31,25,-31,25,25,25,]),'EEQUALS':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,26,-32,-33,-34,-35,-36,-29,-30,26,-31,-31,26,-16,-17,-18,-19,-20,26,-22,-23,-24,-25,26,-27,-28,-31,26,-31,26,-31,26,26,26,]),'GREATER':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,27,-32,-33,-34,-35,-36,-29,-30,27,-31,-31,27,-16,-17,-18,-19,-20,27,-22,-23,27,27,27,-27,-28,-31,27,-31,27,-31,27,27,27,]),'SMALLER':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,28,-32,-33,-34,-35,-36,-29,-30,28,-31,-31,28,-16,-17,-18,-19,-20,28,-22,-23,28,28,28,-27,-28,-31,28,-31,28,-31,28,28,28,]),'AND':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,29,-32,-33,-34,-35,-36,-29,-30,29,-31,-31,29,-16,-17,-18,-19,-20,29,-22,-23,-24,-25,29,-27,-28,-31,29,-31,29,-31,29,29,29,]),'OR':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,30,-32,-33,-34,-35,-36,-29,-30,30,-31,-31,30,-16,-17,-18,-19,-20,30,-22,-23,-24,-25,30,-27,-28,-31,30,-31,30,-31,30,30,30,]),'NOTEQUALS':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,31,-32,-33,-34,-35,-36,-29,-30,31,-31,-31,31,-16,-17,-18,-19,-20,31,-22,-23,-24,-25,31,-27,-28,-31,31,-31,31,-31,31,31,31,]),'GEQUAL':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,32,-32,-33,-34,-35,-36,-29,-30,32,-31,-31,32,-16,-17,-18,-19,-20,32,-22,-23,32,32,32,-27,-28,-31,32,-31,32,-31,32,32,32,]),'SEQUAL':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,33,-32,-33,-34,-35,-36,-29,-30,33,-31,-31,33,-16,-17,-18,-19,-20,33,-22,-23,33,33,33,-27,-28,-31,33,-31,33,-31,33,33,33,]),'INCREMENT':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,34,-32,-33,-34,-35,-36,-29,-30,34,-31,-31,34,-16,-17,-18,-19,-20,34,-22,-23,-24,-25,34,-27,-28,-31,34,-31,34,-31,34,34,34,]),'DECREMENT':([5,6,12,13,14,15,16,34,35,38,39,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,68,69,74,75,77,86,],[-31,35,-32,-33,-34,-35,-36,-29,-30,35,-31,-31,35,-16,-17,-18,-19,-20,35,-22,-23,-24,-25,35,-27,-28,-31,35,-31,35,-31,35,35,35,]),'LPARENTHESIS':([8,46,47,79,],[37,66,67,84,]),'LCURLY':([10,12,13,14,15,16,34,35,38,39,48,49,50,51,52,53,54,55,56,57,58,59,60,83,],[40,-32,-33,-34,-35,-36,-29,-30,64,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,85,]),'RPARENTHESIS':([12,13,14,15,16,34,35,39,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,67,74,75,77,86,],[-32,-33,-34,-35,-36,-29,-30,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,70,71,76,80,81,82,88,]),'PUSH':([20,],[46,]),'POP':([20,],[47,]),'WHILE':([73,],[79,]),'ELSE':([78,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statements':([0,17,40,],[2,42,65,]),'empty':([0,],[3,]),'statement':([0,17,18,40,64,85,],[4,4,43,4,72,87,]),'expr':([0,9,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,37,40,61,64,66,67,84,85,],[6,38,6,6,45,48,49,50,51,52,53,54,55,56,57,58,59,60,63,6,69,6,75,77,86,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statements','start',1,'p_start','parser.py',19),
  ('start -> empty','start',1,'p_start','parser.py',20),
  ('statements -> statements SEMIC statements','statements',3,'p_statements_mul','parser.py',32),
  ('statements -> statements','statements',1,'p_statements_mul','parser.py',33),
  ('statements -> statement SEMIC statement','statements',3,'p_statements','parser.py',42),
  ('statements -> statement','statements',1,'p_statements','parser.py',43),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',51),
  ('statement -> ID EQUALS expr','statement',3,'p_statement_equal','parser.py',58),
  ('statement -> ID EQUALS ID','statement',3,'p_statement_equal_ass','parser.py',64),
  ('statement -> DECLARE ID EQUALS expr','statement',4,'p_statement_declare','parser.py',70),
  ('statement -> DECLARE ID EQUALS ID','statement',4,'p_statement_declare_id','parser.py',76),
  ('statement -> DECLARE ID','statement',2,'p_statement_declare_only','parser.py',82),
  ('statement -> PRINT LPARENTHESIS ID RPARENTHESIS','statement',4,'p_statement_print','parser.py',88),
  ('statement -> PRINT LPARENTHESIS expr RPARENTHESIS','statement',4,'p_statement_print_expr','parser.py',94),
  ('statement -> expr','statement',1,'p_statement','parser.py',102),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_divide','parser.py',108),
  ('expr -> expr MULTIPLY expr','expr',3,'p_expr_multiply','parser.py',112),
  ('expr -> expr ADD expr','expr',3,'p_expr_add','parser.py',116),
  ('expr -> expr SUBTRACT expr','expr',3,'p_expr_subtract','parser.py',120),
  ('expr -> expr MODULUS expr','expr',3,'p_binary_opr','parser.py',126),
  ('expr -> expr EEQUALS expr','expr',3,'p_binary_opr','parser.py',127),
  ('expr -> expr GREATER expr','expr',3,'p_binary_opr','parser.py',128),
  ('expr -> expr SMALLER expr','expr',3,'p_binary_opr','parser.py',129),
  ('expr -> expr AND expr','expr',3,'p_binary_opr','parser.py',130),
  ('expr -> expr OR expr','expr',3,'p_binary_opr','parser.py',131),
  ('expr -> expr NOTEQUALS expr','expr',3,'p_binary_opr','parser.py',132),
  ('expr -> expr GEQUAL expr','expr',3,'p_binary_opr','parser.py',133),
  ('expr -> expr SEQUAL expr','expr',3,'p_binary_opr','parser.py',134),
  ('expr -> expr INCREMENT','expr',2,'p_unary_opr','parser.py',140),
  ('expr -> expr DECREMENT','expr',2,'p_unary_opr','parser.py',141),
  ('expr -> ID','expr',1,'p_expr_ID','parser.py',148),
  ('expr -> INT','expr',1,'p_num','parser.py',154),
  ('expr -> FLOAT','expr',1,'p_num','parser.py',155),
  ('expr -> STRING','expr',1,'p_num','parser.py',156),
  ('expr -> CHAR','expr',1,'p_num','parser.py',157),
  ('expr -> BOOL','expr',1,'p_num','parser.py',158),
  ('statement -> IF expr LCURLY statement RCURLY','statement',5,'p_conditionals','parser.py',165),
  ('statement -> IF expr LCURLY statement RCURLY ELSE LCURLY statement RCURLY','statement',9,'p_conditionals','parser.py',166),
  ('statement -> DO LCURLY statements RCURLY WHILE LPARENTHESIS expr RPARENTHESIS','statement',8,'p_loop','parser.py',176),
  ('statement -> LIST ID','statement',2,'p_list','parser.py',183),
  ('statement -> ID DOT PUSH LPARENTHESIS expr RPARENTHESIS','statement',6,'p_push','parser.py',189),
  ('statement -> ID DOT PUSH LPARENTHESIS ID RPARENTHESIS','statement',6,'p_push_var','parser.py',195),
  ('statement -> ID DOT POP LPARENTHESIS RPARENTHESIS','statement',5,'p_pop','parser.py',201),
  ('statement -> ID DOT POP LPARENTHESIS expr RPARENTHESIS','statement',6,'p_pop_var','parser.py',207),
]
