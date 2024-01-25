#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import ply.lex as lex
import ply.yacc as yacc

from symtab import Scope, Symbol, SymbolTable
from fundef import Fundef
from llvmcode import *
from operand import OType, Operand

symtable = SymbolTable()
varscope = Scope.GLOBAL_VAR
## トークン名のリスト
tokens = (
    'BEGIN', 'DIV', 'DO', 'ELSE', 'END', 'FOR', 'FUNCTION', 'IF',
    'PROCEDURE', 'PROGRAM', 'READ', 'THEN', 'TO', 'VAR', 'WHILE', 'WRITE',
    'PLUS', 'MINUS', 'MULT', 'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE',
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON',
    'PERIOD', 'INTERVAL', 'ASSIGN',
    'IDENT', 'NUMBER'
)

## 予約語の定義
reserved = {
    'begin': 'BEGIN',
    'div': 'DIV',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'read': 'READ',
    'then': 'THEN',
    'to': 'TO',
    'var': 'VAR',
    'while': 'WHILE',
    'write': 'WRITE'
}

### 基本シンボルトークンを切り出すルール
t_PLUS  = '\+'
t_MINUS = '-'
t_MULT  = '\*'
t_EQ      = '='
t_NEQ     = '<>'
t_LT      = '<'
t_LE      = '<='
t_GT      = '>'
t_GE      = '>='
t_LPAREN  = '\('
t_RPAREN  = '\)'
t_LBRACKET= '\['
t_RBRACKET= '\]'
t_COMMA   = ','
t_SEMICOLON= ';'
t_PERIOD  = '\.'
t_INTERVAL= '\.\.'
t_ASSIGN  = ':='
# コメントおよび空白・タブを無視するルール
t_ignore_COMMENT = '\#.*'
t_ignore = ' \t'
## アクションを伴うトークンルール
# 変数名・手続き名などの識別子を切り出すルール
def t_IDENT(t):
    '[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

# 数値を切り出すルール
def t_NUMBER(t):
    '[1-9][0-9]*|0'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Line %d: integer value %s is too large" % t.lineno, t.value)
        t.value = 0
    return t

# 改行を読んだときの処理
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# エラー処理
def t_error(t):
    print("不正な文字「", t.value[0], "」")
    t.lexer.skip(1)


#################################################################
# 解析に必要な変数を宣言しておく
#################################################################

symtable = SymbolTable()
varscope = Scope.GLOBAL_VAR

fundefs = []				# 生成した関数定義（Fundef）のリスト

useWrite = False			# write関数が使用されているかのフラグ
useRead  = False			# read関数が使用されているかのフラグ

labelNum = 1

labels = []

def addCode(l:LLVMCode):
    ''' 現在の関数定義オブジェクトの codes に命令 l を追加 '''
    fundefs[-1].codes.append(l)

def getRegister():
    ''' 新たなレジスタ番号をもつ Operand オブジェクトを返す '''
    return Operand(OType.NUMBERED_REG, val=fundefs[-1].getNewRegNo())

#################################################################
# ここから先に構文規則を書く
#################################################################

def p_program(p):
    '''
    program : PROGRAM IDENT SEMICOLON outblock PERIOD
    '''
    with open("result.ll", "w") as fout:
        # 大域変数ごとに common global 命令を出力
        for t in symtable.rows:
            
            if t.scope == Scope.GLOBAL_VAR:
                print(LLVMCodeGlobal(t.name), file=fout)
        print('', file=fout)

        # 関数定義を出力
        for f in fundefs:
            f.print(fout)

        # printfやscanf関数の宣言と書式を表す文字列定義を出力
        if useWrite:
            LLVMCodeCallPrintf.printDeclare(fout)
            LLVMCodeCallPrintf.printFormat(fout)
        if useRead:
            LLVMCodeCallScanf.printDeclare(fout)
            LLVMCodeCallScanf.printFormat(fout)

def p_outblock(p):
    '''
    outblock : var_decl_part subprog_decl_part outblock_act statement
    '''
    # 規則の右辺に outblock_act が追加されていることに注意!!

    # 還元時に「ret i32 0」命令を追加
    addCode(LLVMCodeRet('i32', Operand(OType.CONSTANT, val=0)))

def p_outblock_act(p):
    '''
    outblock_act :
    '''
    # メイン処理に対する関数定義オブジェクトを生成(名前は main とする）
    fundefs.append(Fundef('main', 'i32'))


def p_var_decl_part(p):
    '''
    var_decl_part : var_decl_list SEMICOLON
                  |
    '''
def p_var_decl_list(p):
    '''
    var_decl_list : var_decl_list SEMICOLON var_decl
                  | var_decl
    '''
def p_var_decl(p):
    '''
    var_decl : VAR id_list
    '''

def p_subprog_decl_part(p):
    '''
    subprog_decl_part : subprog_decl_list SEMICOLON
                      |
    '''
def p_subprog_decl_list(p):
    '''
    subprog_decl_list : subprog_decl_list SEMICOLON subprog_decl
                      | subprog_decl
    '''

def p_subprog_decl(p):
    '''    
    subprog_decl : proc_decl
    '''

def p_proc_decl(p):
    '''
    proc_decl : PROCEDURE proc_name LPAREN proc_act2 RPAREN SEMICOLON inblock
         | PROCEDURE proc_name LPAREN act_proc_args_set id_list act_proc_args_done RPAREN SEMICOLON inblock
    '''
    symtable.delete()
    global varscope
    varscope = Scope.GLOBAL_VAR
    addCode(LLVMCodeRet('void'))

def p_proc_act2(p):
    '''
    proc_act2 :
    '''
    fundefs.append(Fundef(p[-2], 'void'))


def p_act_proc_args_done(p):
    '''
    act_proc_args_done :
    '''
    # fundef = fundefs[-1]
    # fundef.setArgs(p[-1])
    # fundefs[-1] = fundef
    # global varscope
    # varscope = Scope.LOCAL_VAR
    fundefs.append(Fundef(p[-4], 'void', p[-1]))
    global varscope
    varscope = Scope.LOCAL_VAR


def p_act_proc_args_set(p):
    '''
    act_proc_args_set :
    '''
    global varscope
    varscope = Scope.PARAM
    

def p_proc_name(p):
    '''
    proc_name : IDENT
    '''
    global varscope
    varscope = Scope.LOCAL_VAR
    symtable.insert(p[1], Scope.PROC)
    # fundefs.append(Fundef(p[1], 'void'))
    p[0] = p[1]
    

def p_inblock(p):
    '''
    inblock : var_decl_part statement
    '''
    # symtable.delete()
    addCode(LLVMCodeRet('void'))

    
def p_statement_list(p):
    '''statement_list : statement_list SEMICOLON statement
                      | statement'''
    
def p_statement(p):
    '''statement : assignment_statement
                | if_statement
                | while_statement
                | for_statement
                | proc_call_statement
                | null_statement
                | block_statement
                | read_statement
                | write_statement'''
    
def p_assignment_statement(p):
    '''assignment_statement : IDENT ASSIGN expression'''
     
    t = symtable.lookup(p[1])
    if t.scope == Scope.GLOBAL_VAR :
        ptr = Operand(OType.GLOBAL_VAR, name=t.name)
    elif t.scope == Scope.LOCAL_VAR:
        ptr = Operand(OType.NAMED_REG, name=t.name)
    retval = p[3]
    addCode(LLVMCodeStore(retval, ptr))
    

def p_act_assign_ident(p):
    '''act_assign_ident :'''
    addCode(LLVMCodeStore(p[-1], p[-3]))
    p[0] = p[-3]


def p_if_statement(p):
    '''if_statement : act_generate_labels IF condition act_insert_br THEN act_insert_label1 statement act_insert_jump3 act_insert_label2 else_statement act_insert_jump3 act_insert_label3'''
    
def p_act_generate_labels(p):
    '''act_generate_labels : '''
    global labelNum,labels
    childLabels = []
    for i in range(3):
        childLabels.append(Operand(OType.LABEL, val=labelNum))
        labelNum += 1
    labels.append(childLabels)

def p_act_insert_br(p):
    '''act_insert_br :'''
    chileLabels = labels[-1]
    addCode(LLVMCodeBr(chileLabels[0], chileLabels[1], p[-1]))
    
def p_act_insert_label1(p):
    '''act_insert_label1 :'''
    label = labels[-1][0]
    addCode(LLVMCodeLabel(label))
    p[0] = label

def p_act_insert_label2(p):
    '''act_insert_label2 :'''
    label = labels[-1][1]
    addCode(LLVMCodeLabel(label))
    p[0] = label

def p_act_insert_label3(p):
    '''act_insert_label3 :'''
    label = labels[-1][2]
    addCode(LLVMCodeLabel(label))
    p[0] = label
    labels.pop(-1)
        
def p_act_insert_jump1(p):
    '''act_insert_jump1 :'''
    label = labels[-1][0]
    addCode(LLVMCodeBr(label))
    p[0] = label

def p_act_insert_jump2(p):
    '''act_insert_jump2 :'''
    label = labels[-1][1]
    addCode(LLVMCodeBr(label))
    p[0] = label

def p_act_insert_jump3(p):
    '''act_insert_jump3 :'''
    label = labels[-1][2]
    addCode(LLVMCodeBr(label))
    p[0] = label
    
    
    

def p_else_statement(p):
    '''else_statement : ELSE statement
                     |'''
    

def p_while_statement(p):
    '''while_statement : WHILE act_generate_labels act_insert_jump1 act_insert_label1 condition act_insert_br_while DO act_insert_label2 statement act_insert_jump1 act_insert_label3'''

def p_act_insert_br_while(p):
    '''act_insert_br_while :'''
    chileLabels = labels[-1]
    addCode(LLVMCodeBr(chileLabels[1], chileLabels[2], p[-1]))



def p_for_statement(p):
    '''for_statement : FOR act_generate_labels IDENT act_lookup_prev_ident ASSIGN expression act_assign_ident act_insert_jump1 act_insert_label1 TO expression act_insert_br_for act_insert_label2 DO statement act_increment_itr act_insert_jump1 act_insert_label3'''

def p_act_insert_br_for(p):
    '''act_insert_br_for :'''
    ptr = p[-8]
    retval1 = getRegister()
    addCode(LLVMCodeLoad(retval1, ptr))
    retval2 = getRegister()
    cmptype = CmpType.getCmpType("<=")
    addCode(LLVMCodeCmp(retval2, cmptype, retval1, p[-1]))
    chileLabels = labels[-1]
    addCode(LLVMCodeBr(chileLabels[1], chileLabels[2], retval2))
    p[0] = retval1

def p_act_increment_itr(p):
    '''act_increment_itr :'''
    retval1 = p[-4]
    retval2 = getRegister()
    arg1 = Operand(OType.CONSTANT, val=1)
    addCode(LLVMCodeAdd(retval2, retval1, arg1))
    addCode(LLVMCodeStore(retval2, p[-9]))


def p_for_act1(p):
    '''for_act1 :'''
    symtable.lookup(p[-3])
    
def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression'''
    if len(p) == 2:
        if type(p[1]) == str:
            t = symtable.lookup(p[1])
            if t.scope == Scope.GLOBAL_VAR:
                ptr = Operand(OType.GLOBAL_VAR, name=t.name)
            elif t.scope == Scope.LOCAL_VAR:
                ptr = Operand(OType.NAMED_REG, name=t.name)
            elif t.scope == Scope.PARAM:
                ptr = Operand(OType.NAMED_REG, name=t.name)
            retval = getRegister()
            addCode(LLVMCodeLoad(retval,ptr))
            p[0] = f"i32 {retval}"
        else:
            p[0] = f"i32 {p[1]}"
    else:
        if type(p[3]) == str:
            t = symtable.lookup(p[3])
            if t.scope == Scope.GLOBAL_VAR:
                ptr = Operand(OType.GLOBAL_VAR, name=t.name)
            elif t.scope == Scope.LOCAL_VAR:
                ptr = Operand(OType.NAMED_REG, name=t.name)
            elif t.scope == Scope.PARAM:
                ptr = Operand(OType.NAMED_REG, name=t.name)
            retval = getRegister()
            addCode(LLVMCodeLoad(retval, ptr))
            p[0] = f"{p[1]}, i32 {retval}"
        else:
            p[0] = f"{p[1]}, i32 {p[3]}"

def p_proc_call_name(p):
    '''proc_call_name : IDENT'''
    symtable.lookup(p[1])
    p[0] = p[1]

def p_proc_call_statement(p):
    '''proc_call_statement : proc_call_name LPAREN RPAREN
                           | proc_call_name LPAREN arg_list RPAREN
                           
    '''

    if len(p) == 4:
        addCode(LLVMCodeCall(p[1], 'void'))
    else:
        addCode(LLVMCodeCall(p[1],'void', p[3]))


def p_block_statement(p):
    '''block_statement : BEGIN statement_list END'''
    
def p_act_lookup_prev_ident(p):
    '''act_lookup_prev_ident :'''
    t = symtable.lookup(p[-1])
    if t.scope == Scope.GLOBAL_VAR or t.scope == Scope.PROC:
        ptr = Operand(OType.GLOBAL_VAR, name=t.name)
    elif t.scope == Scope.LOCAL_VAR or t.scope == Scope.PARAM:
        ptr = Operand(OType.NAMED_REG, name=t.name)
    p[0] = ptr

def p_read_statement(p):
    '''
    read_statement : READ LPAREN IDENT RPAREN
    '''
    global useRead
    useRead = True

    t = symtable.lookup(p[3])
    if t.scope == Scope.GLOBAL_VAR:
        ptr = Operand(OType.GLOBAL_VAR, name=t.name)
    if t.scope == Scope.LOCAL_VAR:
        ptr = Operand(OType.NAMED_REG, name=t.name)
    if t.scope == Scope.PARAM:
        ptr = Operand(OType.NAMED_REG, name=t.name) 

    addCode(LLVMCodeCallScanf(getRegister(), ptr))

def p_write_statement(p):
    '''
    write_statement : WRITE LPAREN expression RPAREN
    '''
    global useWrite
    useWrite = True
    arg = p[3]
    addCode(LLVMCodeCallPrintf(getRegister(), arg))

def p_null_statement(p):
    '''null_statement :'''

def p_condition(p):
    '''condition : expression EQ expression
                 | expression NEQ expression
                 | expression LT expression
                 | expression LE expression
                 | expression GT expression
                 | expression GE expression'''
    cmptype = CmpType.getCmpType(p[2])
    retval = getRegister()
    addCode(LLVMCodeCmp(retval, cmptype, p[1], p[3]))
    p[0] = retval

def p_expression(p):
    '''
    expression : term
               | MINUS term
               | expression PLUS term
               | expression MINUS term
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        arg = p[2]
        retval = getRegister()
        addCode(LLVMCodeSub(retval, Operand(OType.CONSTANT, val=0), arg))
        p[0] = retval
    else:
        if p[2] == "+":
            arg1 = p[1]
            arg2 = p[3]
            retval = getRegister()
            addCode(LLVMCodeAdd(retval, arg1, arg2))
            p[0] = retval
        elif p[2] == "-":
            arg1 = p[1]
            arg2 = p[3]
            retval = getRegister()
            addCode(LLVMCodeSub(retval, arg1, arg2))
            p[0] = retval   


def p_term(p):
    '''
    term : factor
         | term MULT factor
         | term DIV factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == "*":
            arg1 = p[1]
            arg2 = p[3]
            retval = getRegister()
            addCode(LLVMCodeMul(retval, arg1, arg2))
            p[0] = retval
        elif p[2] == "div":
            arg1 = p[1]
            arg2 = p[3]
            retval = getRegister()
            addCode(LLVMCodeDiv(retval, arg1, arg2))
            p[0] = retval



def p_factor(p):
    '''
    factor : var_name
           | number
           | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_var_name(p):
    '''
    var_name : IDENT
    '''
    t = symtable.lookup(p[1])
    if t.scope == Scope.PARAM:
        p[0] = Operand(OType.NAMED_REG, p[1])
    else:
        if t.scope == Scope.GLOBAL_VAR:
            ptr = Operand(OType.GLOBAL_VAR, name=t.name)
        elif t.scope == Scope.LOCAL_VAR:
            ptr = Operand(OType.NAMED_REG, name=t.name)
        retval = getRegister()
        addCode(LLVMCodeLoad(retval, ptr))        
        p[0] = retval
    
    # if ptr.name in args:
    #     p[0] = ptr
    # else:
    #     retval = getRegister()
    #     addCode(LLVMCodeLoad(retval, ptr))
    #     p[0] = retval

    # retval = getRegister()
    # addCode(LLVMCodeLoad(retval, ptr))
    # p[0] = retval

def p_number(p):
    '''
    number : NUMBER
    '''
    p[0] = Operand(OType.CONSTANT, val=int(p[1]))

def p_id_list(p):
    '''id_list : IDENT
               | id_list COMMA IDENT'''
    
    if len(p) == 2:
        name=p[1]
        if varscope == Scope.PARAM:
            p[0] = f"i32 %{name}"
    else:
        name=p[3]
        if varscope == Scope.PARAM:
            p[0] = f"{p[1]}, i32 %{p[3]}"
    symtable.insert(name, varscope)
    if varscope == Scope.LOCAL_VAR:
        retval = Operand(OType.NAMED_REG, name)
        addCode(LLVMCodeAlloca(retval))

    
#################################################################
# 構文解析エラー時の処理
#################################################################

# def p_error(p):
#     if p:
#         # p.type, p.value, p.linenoを使ってエラーの処理を書く
#         print("Syntax error at token", p.type, p.value, p.lineno)

#     else:
#         print("Syntax error at EOF")
    
def find_column(input, token):
    ''' トークンの列位置を特定する補助関数 '''
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

def p_error(p):
    if p:
        column = find_column(data, p)
        print(f"Syntax error at '{p.type}' token, value '{p.value}', line {p.lineno}, column {column}")
        # 前後のトークンの情報を提供する
        context_start = max(p.lexpos - 10, 0)
        context_end = min(p.lexpos + 10, len(data))
        context = data[context_start:context_end]
        print(f"Context: ...{context}...")
    else:
        print("Syntax error at EOF")

#################################################################
# メインの処理
#################################################################

if __name__ == "__main__":
    lexer = lex.lex(debug=0)  # 字句解析器
    yacc.yacc()  # 構文解析器

    # ファイルを開いて
    data = open(sys.argv[1]).read()
    # 解析を実行
    yacc.parse(data, lexer=lexer)
