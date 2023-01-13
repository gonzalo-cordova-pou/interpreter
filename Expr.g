grammar Expr;
root : declareFunction* expr? EOF ;

declareFunction : ID_FUNCTION ID* '{' block '}' ;

block : instruc+ ;

instruc : '(' instruc ')'                          # parenthesizedInstruc
    | expr                                         # write
    | ID '<-' expr                                 # assignation
    | 'if' expr  '{' block '}'                     # if
    | 'if' expr '{' block '}' 'else' '{' block '}' # ifElse
    | 'while' expr '{' block '}'                   # while
    ;

expr : '(' expr ')'                                # parenthesizedExpr
    | ID_FUNCTION expr*                            # functionCall
    | binaryOperation                              # binaryExpr
    | 'not' expr                                   # not
    | 'true' | 'false'                             # bool
    | NUM                                          # numExpr
    | ID                                           # varExpr
    ;

// binary operations
binaryOperation : expr '+' expr
    | expr '-' expr
    | <assoc=right> expr '*' expr
    | expr '^' expr
    | expr '=' expr
    | expr '!=' expr
    | expr '<' expr
    | expr '>' expr
    | expr '<=' expr
    | expr '>=' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr '/' expr
    ;

ID : [a-z][a-zA-Z0-9_]* ;
ID_FUNCTION : [A-Z][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;