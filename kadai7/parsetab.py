
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BEGIN COMMA DIV DO ELSE END EQ FOR FUNCTION GE GT IDENT IF INTERVAL LBRACKET LE LPAREN LT MINUS MULT NEQ NUMBER PERIOD PLUS PROCEDURE PROGRAM RBRACKET READ RPAREN SEMICOLON THEN TO VAR WHILE WRITE\n    program : PROGRAM IDENT SEMICOLON outblock PERIOD\n    \n    outblock : var_decl_part subprog_decl_part outblock_act statement\n    \n    outblock_act :\n    \n    var_decl_part : var_decl_list SEMICOLON\n                  |\n    \n    var_decl_list : var_decl_list SEMICOLON var_decl\n                  | var_decl\n    \n    var_decl : VAR id_list\n    \n    subprog_decl_part : subprog_decl_list SEMICOLON\n                      |\n    \n    subprog_decl_list : subprog_decl_list SEMICOLON subprog_decl\n                      | subprog_decl\n        \n    subprog_decl : proc_decl\n                 | func_decl\n    \n    func_decl : FUNCTION func_name LPAREN func_act2 RPAREN SEMICOLON inblock\n                | FUNCTION func_name LPAREN act_func_args_set id_list act_func_args_done RPAREN SEMICOLON inblock\n    \n    func_name : IDENT\n    \n    func_act2 :\n    \n    act_func_args_set :\n    \n    act_func_args_done :\n    \n    proc_decl : PROCEDURE proc_name LPAREN proc_act2 RPAREN SEMICOLON inblock\n         | PROCEDURE proc_name LPAREN act_proc_args_set id_list act_proc_args_done RPAREN SEMICOLON inblock\n    \n    proc_act2 :\n    \n    act_proc_args_done :\n    \n    act_proc_args_set :\n    \n    proc_name : IDENT\n    \n    inblock : var_decl_part statement\n    statement_list : statement_list SEMICOLON statement\n                      | statementstatement : assignment_statement\n                | if_statement\n                | while_statement\n                | for_statement\n                | proc_call_statement\n                | null_statement\n                | block_statement\n                | read_statement\n                | write_statementassignment_statement : IDENT ASSIGN expressionact_assign_ident :if_statement : act_generate_labels IF condition act_insert_br THEN act_insert_label1 statement act_insert_jump3 act_insert_label2 else_statement act_insert_jump3 act_insert_label3act_generate_labels : act_insert_br :act_insert_label1 :act_insert_label2 :act_insert_label3 :act_insert_jump1 :act_insert_jump3 :else_statement : ELSE statement\n                     |while_statement : WHILE act_generate_labels act_insert_jump1 act_insert_label1 condition act_insert_br_while DO act_insert_label2 statement act_insert_jump1 act_insert_label3act_insert_br_while :for_statement : FOR act_generate_labels IDENT act_lookup_prev_ident ASSIGN expression act_assign_ident act_insert_jump1 act_insert_label1 TO expression act_insert_br_for act_insert_label2 DO statement act_increment_itr act_insert_jump1 act_insert_label3act_insert_br_for :act_increment_itr :arg_list : expression\n                | arg_list COMMA expressionproc_call_name : IDENTproc_call_statement : proc_call_name LPAREN RPAREN\n                           | proc_call_name LPAREN arg_list RPAREN\n                           \n    block_statement : BEGIN statement_list ENDact_lookup_prev_ident :\n    read_statement : READ LPAREN IDENT RPAREN\n    \n    write_statement : WRITE LPAREN expression RPAREN\n    null_statement :condition : expression EQ expression\n                 | expression NEQ expression\n                 | expression LT expression\n                 | expression LE expression\n                 | expression GT expression\n                 | expression GE expression\n    expression : term\n               | MINUS term\n               | expression PLUS term\n               | expression MINUS term\n    \n    term : factor\n         | term MULT factor\n         | term DIV factor\n    \n    factor : var_name\n           | number\n           | LPAREN expression RPAREN\n           | func_call\n    \n    func_call : IDENT LPAREN RPAREN\n              | IDENT LPAREN arg_list RPAREN\n    \n    var_name : IDENT\n    \n    number : NUMBER\n    id_list : IDENT\n               | id_list COMMA IDENT'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,10,],[0,-1,]),'IDENT':([2,4,6,9,11,16,17,18,21,22,28,41,42,44,48,49,51,52,53,54,55,58,59,61,63,67,71,76,82,89,90,91,92,93,97,98,99,100,101,102,103,106,110,112,121,129,132,137,141,142,144,149,155,157,165,],[3,-5,-10,20,-3,24,26,-4,39,-9,50,-42,-42,39,-25,-19,64,64,-47,77,64,83,64,20,20,64,64,-44,39,64,64,64,64,64,64,64,64,64,64,64,64,64,-5,-5,-44,64,39,39,-5,-5,-45,39,39,64,39,]),'SEMICOLON':([3,7,8,12,13,14,15,18,19,20,27,30,31,32,33,34,35,36,37,38,44,47,50,56,57,64,65,66,68,69,70,72,73,78,81,82,85,87,94,105,107,108,109,110,112,114,116,117,118,119,120,121,131,132,133,134,135,136,137,140,141,142,143,144,146,147,148,149,151,152,154,155,156,158,159,160,162,165,166,167,168,169,],[4,18,-7,22,-12,-13,-14,-4,-8,-87,-6,-30,-31,-32,-33,-34,-35,-36,-37,-38,-65,-11,-88,82,-29,-85,-39,-72,-76,-79,-80,-82,-86,-59,-61,-65,110,112,-73,-60,-28,-63,-64,-5,-5,-83,-74,-75,-77,-78,-81,-44,-21,-65,141,-15,142,-84,-65,-27,-5,-5,-48,-45,-22,-16,-45,-65,-50,-47,-48,-65,-46,-46,-49,-51,-41,-65,-55,-47,-46,-53,]),'PROCEDURE':([4,6,18,22,],[-5,16,-4,16,]),'FUNCTION':([4,6,18,22,],[-5,17,-4,17,]),'WHILE':([4,6,11,18,21,22,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,41,-9,41,41,-5,-5,-44,41,41,-5,-5,-45,41,41,41,]),'FOR':([4,6,11,18,21,22,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,42,-9,42,42,-5,-5,-44,42,42,-5,-5,-45,42,42,42,]),'BEGIN':([4,6,11,18,21,22,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,44,-9,44,44,-5,-5,-44,44,44,-5,-5,-45,44,44,44,]),'READ':([4,6,11,18,21,22,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,45,-9,45,45,-5,-5,-44,45,45,-5,-5,-45,45,45,45,]),'WRITE':([4,6,11,18,21,22,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,46,-9,46,46,-5,-5,-44,46,46,-5,-5,-45,46,46,46,]),'IF':([4,6,11,18,21,22,40,44,82,110,112,121,132,137,141,142,144,149,155,165,],[-5,-10,-3,-4,-42,-9,52,-42,-42,-5,-5,-44,-42,-42,-5,-5,-45,-42,-42,-42,]),'PERIOD':([4,5,6,11,18,21,22,29,30,31,32,33,34,35,36,37,38,64,65,66,68,69,70,72,73,78,81,94,105,108,109,114,116,117,118,119,120,121,136,137,143,144,148,149,151,152,154,155,156,158,159,160,162,165,166,167,168,169,],[-5,10,-10,-3,-4,-65,-9,-2,-30,-31,-32,-33,-34,-35,-36,-37,-38,-85,-39,-72,-76,-79,-80,-82,-86,-59,-61,-73,-60,-63,-64,-83,-74,-75,-77,-78,-81,-44,-84,-65,-48,-45,-45,-65,-50,-47,-48,-65,-46,-46,-49,-51,-41,-65,-55,-47,-46,-53,]),'VAR':([4,18,110,112,141,142,],[9,9,9,9,9,9,]),'COMMA':([19,20,50,64,66,68,69,70,72,73,79,80,86,88,94,114,115,116,117,118,119,120,130,136,],[28,-87,-88,-85,-72,-76,-79,-80,-82,-86,106,-56,28,28,-73,-83,106,-74,-75,-77,-78,-81,-57,-84,]),'RPAREN':([20,48,49,50,55,60,62,64,66,68,69,70,72,73,79,80,83,84,86,88,89,94,95,111,113,114,115,116,117,118,119,120,130,136,],[-87,-23,-18,-88,78,85,87,-85,-72,-76,-79,-80,-82,-86,105,-56,108,109,-24,-20,114,-73,120,133,135,-83,136,-74,-75,-77,-78,-81,-57,-84,]),'LPAREN':([23,24,25,26,39,41,43,45,46,51,52,53,55,59,64,67,71,76,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[48,-26,49,-17,-58,-42,55,58,59,71,71,-47,71,71,89,71,71,-44,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'END':([30,31,32,33,34,35,36,37,38,44,56,57,64,65,66,68,69,70,72,73,78,81,82,94,105,107,108,109,114,116,117,118,119,120,121,136,137,143,144,148,149,151,152,154,155,156,158,159,160,162,165,166,167,168,169,],[-30,-31,-32,-33,-34,-35,-36,-37,-38,-65,81,-29,-85,-39,-72,-76,-79,-80,-82,-86,-59,-61,-65,-73,-60,-28,-63,-64,-83,-74,-75,-77,-78,-81,-44,-84,-65,-48,-45,-45,-65,-50,-47,-48,-65,-46,-46,-49,-51,-41,-65,-55,-47,-46,-53,]),'ELSE':([30,31,32,33,34,35,36,37,38,64,65,66,68,69,70,72,73,78,81,94,105,108,109,114,116,117,118,119,120,121,136,137,143,144,148,149,151,152,154,155,156,158,159,160,162,165,166,167,168,169,],[-30,-31,-32,-33,-34,-35,-36,-37,-38,-85,-39,-72,-76,-79,-80,-82,-86,-59,-61,-73,-60,-63,-64,-83,-74,-75,-77,-78,-81,-44,-84,-65,-48,-45,-45,-65,155,-47,-48,-65,-46,-46,-49,-51,-41,-65,-55,-47,-46,-53,]),'ASSIGN':([39,77,104,],[51,-62,129,]),'MINUS':([41,51,52,53,55,59,64,65,66,68,69,70,71,72,73,75,76,80,84,89,94,95,97,98,99,100,101,102,103,106,114,116,117,118,119,120,122,123,124,125,126,127,129,130,136,139,157,161,],[-42,67,67,-47,67,67,-85,91,-72,-76,-79,-80,67,-82,-86,91,-44,91,91,67,-73,91,67,67,67,67,67,67,67,67,-83,-74,-75,-77,-78,-81,91,91,91,91,91,91,67,91,-84,91,67,91,]),'NUMBER':([41,51,52,53,55,59,67,71,76,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[-42,73,73,-47,73,73,73,73,-44,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'MULT':([64,66,68,69,70,72,73,94,114,116,117,118,119,120,136,],[-85,92,-76,-79,-80,-82,-86,92,-83,92,92,-77,-78,-81,-84,]),'DIV':([64,66,68,69,70,72,73,94,114,116,117,118,119,120,136,],[-85,93,-76,-79,-80,-82,-86,93,-83,93,93,-77,-78,-81,-84,]),'PLUS':([64,65,66,68,69,70,72,73,75,80,84,94,95,114,116,117,118,119,120,122,123,124,125,126,127,130,136,139,161,],[-85,90,-72,-76,-79,-80,-82,-86,90,90,90,-73,90,-83,-74,-75,-77,-78,-81,90,90,90,90,90,90,90,-84,90,90,]),'EQ':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,97,-73,-83,-74,-75,-77,-78,-81,-84,]),'NEQ':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,98,-73,-83,-74,-75,-77,-78,-81,-84,]),'LT':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,99,-73,-83,-74,-75,-77,-78,-81,-84,]),'LE':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,100,-73,-83,-74,-75,-77,-78,-81,-84,]),'GT':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,101,-73,-83,-74,-75,-77,-78,-81,-84,]),'GE':([64,66,68,69,70,72,73,75,94,114,116,117,118,119,120,136,],[-85,-72,-76,-79,-80,-82,-86,102,-73,-83,-74,-75,-77,-78,-81,-84,]),'THEN':([64,66,68,69,70,72,73,74,94,96,114,116,117,118,119,120,122,123,124,125,126,127,136,],[-85,-72,-76,-79,-80,-82,-86,-43,-73,121,-83,-74,-75,-77,-78,-81,-66,-67,-68,-69,-70,-71,-84,]),'DO':([64,66,68,69,70,72,73,94,114,116,117,118,119,120,122,123,124,125,126,127,128,136,138,161,163,164,],[-85,-72,-76,-79,-80,-82,-86,-73,-83,-74,-75,-77,-78,-81,-66,-67,-68,-69,-70,-71,-52,-84,144,-54,-45,165,]),'TO':([64,66,68,69,70,72,73,94,114,116,117,118,119,120,136,139,145,150,153,],[-85,-72,-76,-79,-80,-82,-86,-73,-83,-74,-75,-77,-78,-81,-84,-40,-47,-44,157,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'outblock':([4,],[5,]),'var_decl_part':([4,110,112,141,142,],[6,132,132,132,132,]),'var_decl_list':([4,110,112,141,142,],[7,7,7,7,7,]),'var_decl':([4,18,110,112,141,142,],[8,27,8,8,8,8,]),'subprog_decl_part':([6,],[11,]),'subprog_decl_list':([6,],[12,]),'subprog_decl':([6,22,],[13,47,]),'proc_decl':([6,22,],[14,14,]),'func_decl':([6,22,],[15,15,]),'id_list':([9,61,63,],[19,86,88,]),'outblock_act':([11,],[21,]),'proc_name':([16,],[23,]),'func_name':([17,],[25,]),'statement':([21,44,82,132,137,149,155,165,],[29,57,107,140,143,152,159,166,]),'assignment_statement':([21,44,82,132,137,149,155,165,],[30,30,30,30,30,30,30,30,]),'if_statement':([21,44,82,132,137,149,155,165,],[31,31,31,31,31,31,31,31,]),'while_statement':([21,44,82,132,137,149,155,165,],[32,32,32,32,32,32,32,32,]),'for_statement':([21,44,82,132,137,149,155,165,],[33,33,33,33,33,33,33,33,]),'proc_call_statement':([21,44,82,132,137,149,155,165,],[34,34,34,34,34,34,34,34,]),'null_statement':([21,44,82,132,137,149,155,165,],[35,35,35,35,35,35,35,35,]),'block_statement':([21,44,82,132,137,149,155,165,],[36,36,36,36,36,36,36,36,]),'read_statement':([21,44,82,132,137,149,155,165,],[37,37,37,37,37,37,37,37,]),'write_statement':([21,44,82,132,137,149,155,165,],[38,38,38,38,38,38,38,38,]),'act_generate_labels':([21,41,42,44,82,132,137,149,155,165,],[40,53,54,40,40,40,40,40,40,40,]),'proc_call_name':([21,44,82,132,137,149,155,165,],[43,43,43,43,43,43,43,43,]),'statement_list':([44,],[56,]),'proc_act2':([48,],[60,]),'act_proc_args_set':([48,],[61,]),'func_act2':([49,],[62,]),'act_func_args_set':([49,],[63,]),'expression':([51,52,55,59,71,89,97,98,99,100,101,102,103,106,129,157,],[65,75,80,84,95,80,122,123,124,125,126,127,75,130,139,161,]),'term':([51,52,55,59,67,71,89,90,91,97,98,99,100,101,102,103,106,129,157,],[66,66,66,66,94,66,66,116,117,66,66,66,66,66,66,66,66,66,66,]),'factor':([51,52,55,59,67,71,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[68,68,68,68,68,68,68,68,68,118,119,68,68,68,68,68,68,68,68,68,68,]),'var_name':([51,52,55,59,67,71,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'number':([51,52,55,59,67,71,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'func_call':([51,52,55,59,67,71,89,90,91,92,93,97,98,99,100,101,102,103,106,129,157,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'condition':([52,103,],[74,128,]),'act_insert_jump1':([53,145,152,167,],[76,150,156,168,]),'arg_list':([55,89,],[79,115,]),'act_insert_br':([74,],[96,]),'act_insert_label1':([76,121,150,],[103,137,153,]),'act_lookup_prev_ident':([77,],[104,]),'act_proc_args_done':([86,],[111,]),'act_func_args_done':([88,],[113,]),'inblock':([110,112,141,142,],[131,134,146,147,]),'act_insert_br_while':([128,],[138,]),'act_assign_ident':([139,],[145,]),'act_insert_jump3':([143,154,],[148,158,]),'act_insert_label2':([144,148,163,],[149,151,164,]),'else_statement':([151,],[154,]),'act_insert_label3':([156,158,168,],[160,162,169,]),'act_insert_br_for':([161,],[163,]),'act_increment_itr':([166,],[167,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENT SEMICOLON outblock PERIOD','program',5,'p_program','compiler.py',126),
  ('outblock -> var_decl_part subprog_decl_part outblock_act statement','outblock',4,'p_outblock','compiler.py',150),
  ('outblock_act -> <empty>','outblock_act',0,'p_outblock_act','compiler.py',159),
  ('var_decl_part -> var_decl_list SEMICOLON','var_decl_part',2,'p_var_decl_part','compiler.py',167),
  ('var_decl_part -> <empty>','var_decl_part',0,'p_var_decl_part','compiler.py',168),
  ('var_decl_list -> var_decl_list SEMICOLON var_decl','var_decl_list',3,'p_var_decl_list','compiler.py',172),
  ('var_decl_list -> var_decl','var_decl_list',1,'p_var_decl_list','compiler.py',173),
  ('var_decl -> VAR id_list','var_decl',2,'p_var_decl','compiler.py',177),
  ('subprog_decl_part -> subprog_decl_list SEMICOLON','subprog_decl_part',2,'p_subprog_decl_part','compiler.py',182),
  ('subprog_decl_part -> <empty>','subprog_decl_part',0,'p_subprog_decl_part','compiler.py',183),
  ('subprog_decl_list -> subprog_decl_list SEMICOLON subprog_decl','subprog_decl_list',3,'p_subprog_decl_list','compiler.py',187),
  ('subprog_decl_list -> subprog_decl','subprog_decl_list',1,'p_subprog_decl_list','compiler.py',188),
  ('subprog_decl -> proc_decl','subprog_decl',1,'p_subprog_decl','compiler.py',193),
  ('subprog_decl -> func_decl','subprog_decl',1,'p_subprog_decl','compiler.py',194),
  ('func_decl -> FUNCTION func_name LPAREN func_act2 RPAREN SEMICOLON inblock','func_decl',7,'p_func_decl','compiler.py',199),
  ('func_decl -> FUNCTION func_name LPAREN act_func_args_set id_list act_func_args_done RPAREN SEMICOLON inblock','func_decl',9,'p_func_decl','compiler.py',200),
  ('func_name -> IDENT','func_name',1,'p_func_name','compiler.py',212),
  ('func_act2 -> <empty>','func_act2',0,'p_func_act2','compiler.py',220),
  ('act_func_args_set -> <empty>','act_func_args_set',0,'p_act_func_args_set','compiler.py',229),
  ('act_func_args_done -> <empty>','act_func_args_done',0,'p_act_func_args_done','compiler.py',236),
  ('proc_decl -> PROCEDURE proc_name LPAREN proc_act2 RPAREN SEMICOLON inblock','proc_decl',7,'p_proc_decl','compiler.py',244),
  ('proc_decl -> PROCEDURE proc_name LPAREN act_proc_args_set id_list act_proc_args_done RPAREN SEMICOLON inblock','proc_decl',9,'p_proc_decl','compiler.py',245),
  ('proc_act2 -> <empty>','proc_act2',0,'p_proc_act2','compiler.py',254),
  ('act_proc_args_done -> <empty>','act_proc_args_done',0,'p_act_proc_args_done','compiler.py',261),
  ('act_proc_args_set -> <empty>','act_proc_args_set',0,'p_act_proc_args_set','compiler.py',275),
  ('proc_name -> IDENT','proc_name',1,'p_proc_name','compiler.py',283),
  ('inblock -> var_decl_part statement','inblock',2,'p_inblock','compiler.py',294),
  ('statement_list -> statement_list SEMICOLON statement','statement_list',3,'p_statement_list','compiler.py',301),
  ('statement_list -> statement','statement_list',1,'p_statement_list','compiler.py',302),
  ('statement -> assignment_statement','statement',1,'p_statement','compiler.py',305),
  ('statement -> if_statement','statement',1,'p_statement','compiler.py',306),
  ('statement -> while_statement','statement',1,'p_statement','compiler.py',307),
  ('statement -> for_statement','statement',1,'p_statement','compiler.py',308),
  ('statement -> proc_call_statement','statement',1,'p_statement','compiler.py',309),
  ('statement -> null_statement','statement',1,'p_statement','compiler.py',310),
  ('statement -> block_statement','statement',1,'p_statement','compiler.py',311),
  ('statement -> read_statement','statement',1,'p_statement','compiler.py',312),
  ('statement -> write_statement','statement',1,'p_statement','compiler.py',313),
  ('assignment_statement -> IDENT ASSIGN expression','assignment_statement',3,'p_assignment_statement','compiler.py',316),
  ('act_assign_ident -> <empty>','act_assign_ident',0,'p_act_assign_ident','compiler.py',328),
  ('if_statement -> act_generate_labels IF condition act_insert_br THEN act_insert_label1 statement act_insert_jump3 act_insert_label2 else_statement act_insert_jump3 act_insert_label3','if_statement',12,'p_if_statement','compiler.py',334),
  ('act_generate_labels -> <empty>','act_generate_labels',0,'p_act_generate_labels','compiler.py',337),
  ('act_insert_br -> <empty>','act_insert_br',0,'p_act_insert_br','compiler.py',346),
  ('act_insert_label1 -> <empty>','act_insert_label1',0,'p_act_insert_label1','compiler.py',351),
  ('act_insert_label2 -> <empty>','act_insert_label2',0,'p_act_insert_label2','compiler.py',357),
  ('act_insert_label3 -> <empty>','act_insert_label3',0,'p_act_insert_label3','compiler.py',363),
  ('act_insert_jump1 -> <empty>','act_insert_jump1',0,'p_act_insert_jump1','compiler.py',370),
  ('act_insert_jump3 -> <empty>','act_insert_jump3',0,'p_act_insert_jump3','compiler.py',382),
  ('else_statement -> ELSE statement','else_statement',2,'p_else_statement','compiler.py',391),
  ('else_statement -> <empty>','else_statement',0,'p_else_statement','compiler.py',392),
  ('while_statement -> WHILE act_generate_labels act_insert_jump1 act_insert_label1 condition act_insert_br_while DO act_insert_label2 statement act_insert_jump1 act_insert_label3','while_statement',11,'p_while_statement','compiler.py',396),
  ('act_insert_br_while -> <empty>','act_insert_br_while',0,'p_act_insert_br_while','compiler.py',399),
  ('for_statement -> FOR act_generate_labels IDENT act_lookup_prev_ident ASSIGN expression act_assign_ident act_insert_jump1 act_insert_label1 TO expression act_insert_br_for act_insert_label2 DO statement act_increment_itr act_insert_jump1 act_insert_label3','for_statement',18,'p_for_statement','compiler.py',406),
  ('act_insert_br_for -> <empty>','act_insert_br_for',0,'p_act_insert_br_for','compiler.py',409),
  ('act_increment_itr -> <empty>','act_increment_itr',0,'p_act_increment_itr','compiler.py',421),
  ('arg_list -> expression','arg_list',1,'p_arg_list','compiler.py',434),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','compiler.py',435),
  ('proc_call_name -> IDENT','proc_call_name',1,'p_proc_call_name','compiler.py',466),
  ('proc_call_statement -> proc_call_name LPAREN RPAREN','proc_call_statement',3,'p_proc_call_statement','compiler.py',471),
  ('proc_call_statement -> proc_call_name LPAREN arg_list RPAREN','proc_call_statement',4,'p_proc_call_statement','compiler.py',472),
  ('block_statement -> BEGIN statement_list END','block_statement',3,'p_block_statement','compiler.py',483),
  ('act_lookup_prev_ident -> <empty>','act_lookup_prev_ident',0,'p_act_lookup_prev_ident','compiler.py',486),
  ('read_statement -> READ LPAREN IDENT RPAREN','read_statement',4,'p_read_statement','compiler.py',496),
  ('write_statement -> WRITE LPAREN expression RPAREN','write_statement',4,'p_write_statement','compiler.py',513),
  ('null_statement -> <empty>','null_statement',0,'p_null_statement','compiler.py',521),
  ('condition -> expression EQ expression','condition',3,'p_condition','compiler.py',524),
  ('condition -> expression NEQ expression','condition',3,'p_condition','compiler.py',525),
  ('condition -> expression LT expression','condition',3,'p_condition','compiler.py',526),
  ('condition -> expression LE expression','condition',3,'p_condition','compiler.py',527),
  ('condition -> expression GT expression','condition',3,'p_condition','compiler.py',528),
  ('condition -> expression GE expression','condition',3,'p_condition','compiler.py',529),
  ('expression -> term','expression',1,'p_expression','compiler.py',537),
  ('expression -> MINUS term','expression',2,'p_expression','compiler.py',538),
  ('expression -> expression PLUS term','expression',3,'p_expression','compiler.py',539),
  ('expression -> expression MINUS term','expression',3,'p_expression','compiler.py',540),
  ('term -> factor','term',1,'p_term','compiler.py',566),
  ('term -> term MULT factor','term',3,'p_term','compiler.py',567),
  ('term -> term DIV factor','term',3,'p_term','compiler.py',568),
  ('factor -> var_name','factor',1,'p_factor','compiler.py',590),
  ('factor -> number','factor',1,'p_factor','compiler.py',591),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','compiler.py',592),
  ('factor -> func_call','factor',1,'p_factor','compiler.py',593),
  ('func_call -> IDENT LPAREN RPAREN','func_call',3,'p_func_call','compiler.py',602),
  ('func_call -> IDENT LPAREN arg_list RPAREN','func_call',4,'p_func_call','compiler.py',603),
  ('var_name -> IDENT','var_name',1,'p_var_name','compiler.py',613),
  ('number -> NUMBER','number',1,'p_number','compiler.py',640),
  ('id_list -> IDENT','id_list',1,'p_id_list','compiler.py',645),
  ('id_list -> id_list COMMA IDENT','id_list',3,'p_id_list','compiler.py',646),
]