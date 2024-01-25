# -*- coding: utf-8 -*-

from enum import Enum

class Scope(Enum):
    ''' Scopeクラス
            記号のタイプを表現
    '''
    GLOBAL_VAR = 0    # 大域変数
    LOCAL_VAR  = 1    # 局所変数
    PROC       = 2    # 手続き
    PARAM      = 3    # 手続きの仮引数

    


class Symbol(object):
    ''' Symbolクラス
            記号（変数，手続き）の情報を表現
    '''

    def __init__(self, name:str, scope:Scope):
        self.name = name     # 名前 : str
        self.scope = scope   # スコープ : Scope

    def __str__(self):
        return f"({self.name},{self.scope})"

    def __repr__(self):
        return str(self)


class SymbolTable(object):
    ''' SymbolTableクラス
            記号表とその操作関数を定義
    '''

    def __init__(self):
        self.rows = []
        #aaaa

    def insert(self, name:str, scope:Scope):
        ''' 記号表への変数・手続きの登録 '''
        self.rows.append(Symbol(name, scope))
        print("-- insert --")
        
        print( (name, scope))

    def lookup(self, name:str) -> Symbol:
        ''' 記号表から変数・手続きの検索 '''
        # for row in self.rows:
        #     if (row.name == name) and (row.scope == Scope.LOCAL_VAR):
        #         print("-- lookup --")
        #         print( (row.name, row.scope))
        #         return row
            
        # for row in self.rows:
        #     if (row.name == name) and (row.scope != Scope.LOCAL_VAR):
        #         print("-- lookup --")
        #         print( (row.name, row.scope))
        #         return row
        for symbol in reversed(self.rows):
            if symbol.name == name:
                print("-- lookup --")
                print( (symbol.name, symbol.scope))
                return symbol


    def delete(self):
        ''' 記号表から局所変数の削除 '''
        # self.rows = [row for row in self.rows if row.scope != (Scope.LOCAL_VAR or Scope.PARAM)]
                
        # print("-- delete --")
        # print([(row.name, row.scope) for row in self.rows])
        for symbol in reversed(self.rows):
            if symbol.scope == Scope.LOCAL_VAR or symbol.scope == Scope.PARAM:
                self.rows.remove(symbol)
            print("-- delete --")
            for i in self.rows:
                print(i)


