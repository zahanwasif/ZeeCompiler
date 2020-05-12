
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startleftANDORleftGREATERSMALLERGEQUALSEQUALleftADDSUBTRACTleftMULTIPLYDIVIDEMODULUSADD AND BOOL CHAR COMMA DECREMENT DIVIDE EEQUALS ELSE EQUALS FLOAT GEQUAL GREATER ID IF INCREMENT INT LCURLY LOOP LPARENTHESIS MODULUS MULTIPLY NOTEQUALS OR PRINT RCURLY RPARENTHESIS SEQUAL SMALLER STRING SUBTRACT VAR\n    start  : statements\n           | empty\n    \n    statements  : statements statement\n                | statement\n    \n    empty :\n    \n    statement : ID EQUALS expr\n    \n    statement : ID EQUALS ID\n    \n    statement : PRINT LPARENTHESIS VAR LPARENTHESIS statement RPARENTHESIS RPARENTHESIS\n              | PRINT LPARENTHESIS statement RPARENTHESIS\n    \n    statement : expr\n    expr : expr DIVIDE exprexpr : expr MULTIPLY exprexpr : expr ADD exprexpr : expr SUBTRACT expr\n    expr : expr MODULUS expr\n         | expr EEQUALS expr\n         | expr GREATER expr\n         | expr SMALLER expr\n         | expr AND expr\n         | expr OR expr\n         | expr NOTEQUALS expr\n         | expr GEQUAL expr\n         | expr SEQUAL expr\n    \n    expr : expr INCREMENT\n         | expr DECREMENT\n\n    \n    expr : ID\n    \n    expr : INT\n           | FLOAT\n           | STRING\n           | CHAR\n           | BOOL\n    \n    statement : IF expr LCURLY statement RCURLY\n              | IF expr LCURLY statement RCURLY ELSE LCURLY statement RCURLY\n    \n    expr : LOOP LPARENTHESIS expr COMMA expr RPARENTHESIS LCURLY statements RCURLY\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,9,10,11,12,13,15,30,31,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,56,60,65,70,71,],[-5,0,-1,-2,-4,-26,-10,-27,-28,-29,-30,-31,-3,-24,-25,-26,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-9,-32,-8,-33,-34,]),'ID':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[5,5,-4,-26,-10,34,-27,-28,-29,-30,-31,-3,36,34,34,34,34,34,34,34,34,34,34,34,34,34,-24,-25,5,-26,34,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,5,5,-9,34,-32,-8,5,5,5,-33,-34,]),'PRINT':([0,2,4,5,6,9,10,11,12,13,15,30,31,32,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,60,65,66,67,69,70,71,],[7,7,-4,-26,-10,-27,-28,-29,-30,-31,-3,-24,-25,7,-26,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,7,7,-9,-32,-8,7,7,7,-33,-34,]),'IF':([0,2,4,5,6,9,10,11,12,13,15,30,31,32,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,60,65,66,67,69,70,71,],[8,8,-4,-26,-10,-27,-28,-29,-30,-31,-3,-24,-25,8,-26,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,8,8,-9,-32,-8,8,8,8,-33,-34,]),'INT':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[9,9,-4,-26,-10,9,-27,-28,-29,-30,-31,-3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-24,-25,9,-26,9,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,9,9,-9,9,-32,-8,9,9,9,-33,-34,]),'FLOAT':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[10,10,-4,-26,-10,10,-27,-28,-29,-30,-31,-3,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-24,-25,10,-26,10,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,10,10,-9,10,-32,-8,10,10,10,-33,-34,]),'STRING':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[11,11,-4,-26,-10,11,-27,-28,-29,-30,-31,-3,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-24,-25,11,-26,11,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,11,11,-9,11,-32,-8,11,11,11,-33,-34,]),'CHAR':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[12,12,-4,-26,-10,12,-27,-28,-29,-30,-31,-3,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-24,-25,12,-26,12,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,12,12,-9,12,-32,-8,12,12,12,-33,-34,]),'BOOL':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[13,13,-4,-26,-10,13,-27,-28,-29,-30,-31,-3,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-24,-25,13,-26,13,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,13,13,-9,13,-32,-8,13,13,13,-33,-34,]),'LOOP':([0,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,55,56,58,60,65,66,67,69,70,71,],[14,14,-4,-26,-10,14,-27,-28,-29,-30,-31,-3,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-24,-25,14,-26,14,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,14,14,-9,14,-32,-8,14,14,14,-33,-34,]),'RCURLY':([4,5,6,9,10,11,12,13,15,30,31,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,56,57,60,65,68,69,70,71,],[-4,-26,-10,-27,-28,-29,-30,-31,-3,-24,-25,-26,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-9,60,-32,-8,70,71,-33,-34,]),'EQUALS':([5,],[16,]),'DIVIDE':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,17,-27,-28,-29,-30,-31,-24,-25,17,-26,-26,17,-11,-12,17,17,-15,17,17,17,17,17,17,17,17,17,17,-34,]),'MULTIPLY':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,18,-27,-28,-29,-30,-31,-24,-25,18,-26,-26,18,-11,-12,18,18,-15,18,18,18,18,18,18,18,18,18,18,-34,]),'ADD':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,19,-27,-28,-29,-30,-31,-24,-25,19,-26,-26,19,-11,-12,-13,-14,-15,19,19,19,19,19,19,19,19,19,19,-34,]),'SUBTRACT':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,20,-27,-28,-29,-30,-31,-24,-25,20,-26,-26,20,-11,-12,-13,-14,-15,20,20,20,20,20,20,20,20,20,20,-34,]),'MODULUS':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,21,-27,-28,-29,-30,-31,-24,-25,21,-26,-26,21,-11,-12,21,21,-15,21,21,21,21,21,21,21,21,21,21,-34,]),'EEQUALS':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,22,-27,-28,-29,-30,-31,-24,-25,22,-26,-26,22,-11,-12,-13,-14,-15,22,-17,-18,-19,-20,22,-22,-23,22,22,-34,]),'GREATER':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,23,-27,-28,-29,-30,-31,-24,-25,23,-26,-26,23,-11,-12,-13,-14,-15,23,-17,-18,23,23,23,-22,-23,23,23,-34,]),'SMALLER':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,24,-27,-28,-29,-30,-31,-24,-25,24,-26,-26,24,-11,-12,-13,-14,-15,24,-17,-18,24,24,24,-22,-23,24,24,-34,]),'AND':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,25,-27,-28,-29,-30,-31,-24,-25,25,-26,-26,25,-11,-12,-13,-14,-15,25,-17,-18,-19,-20,25,-22,-23,25,25,-34,]),'OR':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,26,-27,-28,-29,-30,-31,-24,-25,26,-26,-26,26,-11,-12,-13,-14,-15,26,-17,-18,-19,-20,26,-22,-23,26,26,-34,]),'NOTEQUALS':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,27,-27,-28,-29,-30,-31,-24,-25,27,-26,-26,27,-11,-12,-13,-14,-15,27,-17,-18,-19,-20,27,-22,-23,27,27,-34,]),'GEQUAL':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,28,-27,-28,-29,-30,-31,-24,-25,28,-26,-26,28,-11,-12,-13,-14,-15,28,-17,-18,28,28,28,-22,-23,28,28,-34,]),'SEQUAL':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,29,-27,-28,-29,-30,-31,-24,-25,29,-26,-26,29,-11,-12,-13,-14,-15,29,-17,-18,29,29,29,-22,-23,29,29,-34,]),'INCREMENT':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,30,-27,-28,-29,-30,-31,-24,-25,30,-26,-26,30,-11,-12,-13,-14,-15,30,-17,-18,-19,-20,30,-22,-23,30,30,-34,]),'DECREMENT':([5,6,9,10,11,12,13,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,54,61,71,],[-26,31,-27,-28,-29,-30,-31,-24,-25,31,-26,-26,31,-11,-12,-13,-14,-15,31,-17,-18,-19,-20,31,-22,-23,31,31,-34,]),'RPARENTHESIS':([5,6,9,10,11,12,13,30,31,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,56,59,60,61,62,65,70,71,],[-26,-10,-27,-28,-29,-30,-31,-24,-25,-26,-7,-6,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,56,-9,62,-32,64,65,-8,-33,-34,]),'LPARENTHESIS':([7,14,51,],[32,35,55,]),'LCURLY':([9,10,11,12,13,30,31,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,63,64,71,],[-27,-28,-29,-30,-31,-24,-25,53,-26,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,66,67,-34,]),'COMMA':([9,10,11,12,13,30,31,34,38,39,40,41,42,43,44,45,46,47,48,49,50,54,71,],[-27,-28,-29,-30,-31,-24,-25,-26,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,58,-34,]),'VAR':([32,],[51,]),'ELSE':([60,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statements':([0,67,],[2,69,]),'empty':([0,],[3,]),'statement':([0,2,32,53,55,66,67,69,],[4,15,52,57,59,68,4,15,]),'expr':([0,2,8,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,35,53,55,58,66,67,69,],[6,6,33,37,38,39,40,41,42,43,44,45,46,47,48,49,50,6,54,6,6,61,6,6,6,]),}

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
  ('statements -> statements statement','statements',2,'p_statements','parser.py',29),
  ('statements -> statement','statements',1,'p_statements','parser.py',30),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',39),
  ('statement -> ID EQUALS expr','statement',3,'p_statement_equal','parser.py',46),
  ('statement -> ID EQUALS ID','statement',3,'p_statement_equal_ass','parser.py',52),
  ('statement -> PRINT LPARENTHESIS VAR LPARENTHESIS statement RPARENTHESIS RPARENTHESIS','statement',7,'p_statement_print','parser.py',60),
  ('statement -> PRINT LPARENTHESIS statement RPARENTHESIS','statement',4,'p_statement_print','parser.py',61),
  ('statement -> expr','statement',1,'p_statement','parser.py',74),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_divide','parser.py',80),
  ('expr -> expr MULTIPLY expr','expr',3,'p_expr_multiply','parser.py',84),
  ('expr -> expr ADD expr','expr',3,'p_expr_add','parser.py',88),
  ('expr -> expr SUBTRACT expr','expr',3,'p_expr_subtract','parser.py',92),
  ('expr -> expr MODULUS expr','expr',3,'p_binary_opr','parser.py',98),
  ('expr -> expr EEQUALS expr','expr',3,'p_binary_opr','parser.py',99),
  ('expr -> expr GREATER expr','expr',3,'p_binary_opr','parser.py',100),
  ('expr -> expr SMALLER expr','expr',3,'p_binary_opr','parser.py',101),
  ('expr -> expr AND expr','expr',3,'p_binary_opr','parser.py',102),
  ('expr -> expr OR expr','expr',3,'p_binary_opr','parser.py',103),
  ('expr -> expr NOTEQUALS expr','expr',3,'p_binary_opr','parser.py',104),
  ('expr -> expr GEQUAL expr','expr',3,'p_binary_opr','parser.py',105),
  ('expr -> expr SEQUAL expr','expr',3,'p_binary_opr','parser.py',106),
  ('expr -> expr INCREMENT','expr',2,'p_unary_opr','parser.py',112),
  ('expr -> expr DECREMENT','expr',2,'p_unary_opr','parser.py',113),
  ('expr -> ID','expr',1,'p_expr_ID','parser.py',120),
  ('expr -> INT','expr',1,'p_num','parser.py',126),
  ('expr -> FLOAT','expr',1,'p_num','parser.py',127),
  ('expr -> STRING','expr',1,'p_num','parser.py',128),
  ('expr -> CHAR','expr',1,'p_num','parser.py',129),
  ('expr -> BOOL','expr',1,'p_num','parser.py',130),
  ('statement -> IF expr LCURLY statement RCURLY','statement',5,'p_conditionals','parser.py',137),
  ('statement -> IF expr LCURLY statement RCURLY ELSE LCURLY statement RCURLY','statement',9,'p_conditionals','parser.py',138),
  ('expr -> LOOP LPARENTHESIS expr COMMA expr RPARENTHESIS LCURLY statements RCURLY','expr',9,'p_loop','parser.py',148),
]
