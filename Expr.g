grammar Expr;
root : declareFunction* expr? EOF ;

declareFunction : ID_FUNCTION ID* '{' block '}' ;

block : instruc+ ;

instruc : expr # write
    | ID assign expr # assignation
    | 'if' expr '{' block '}' # if
    | 'if' expr '{' block '}' 'else' '{' block '}' # ifElse
    | 'while' expr '{' block '}' # while
    ;

expr : '(' expr ')'     # parenthesizedExpr
    | ID_FUNCTION expr* # functionCall
    | expr EQ expr      # equalExpr
    | expr NEQ expr     # differentExpr
    | expr LT expr      # lessExpr
    | expr GT expr      # greaterExpr
    | expr LEQ expr     # lessEqualExpr
    | expr GEQ expr     # greaterEqualExpr
    | <assoc=right> expr POW expr # powExpr
    | expr MUL expr # mulExpr
    | expr DIV expr # divExpr
    | expr PLUS expr # addExpr
    | expr MINUS expr # subExpr
    | NUM # numExpr
    | ID # varExpr
    ;

// Variable names
ID : [a-z][a-zA-Z0-9_]* ;
ID_FUNCTION : [A-Z][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
assign : '<-';
EQ : '=';
NEQ : '!=';
LT : '<';
GT : '>';
LEQ : '<=';
GEQ : '>=';
POW : '^' ;
PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/' ;
WS : [ \n]+ -> skip ;