grammar funx;

root : declareFunction* expr? EOF ;

declareFunction : ID_FUNCTION ID* '{' block '}' ;

block : instruc+ ;

instruc : '(' instruc ')'                              # parenthesizedInstruc
    | expr                                             # write
    | ID '<-' expr                                     # assignation
    | 'if' expr  '{' block '}'                         # conditional
    | 'if' expr '{' block '}' 'else' '{' block '}'     # conditional
    | 'while' expr '{' block '}'                       # while
    ;

expr : '(' expr ')'                                    # parenthesizedExpr
    | ID_FUNCTION expr*                                # functionCall
    | <assoc=right> expr '^' expr                      # operationExpr
    | '-' expr                                         # negativeExpr
    | expr ('*' | '/' | '%') expr                      # operationExpr
    | expr ('+' | '-')  expr                           # operationExpr
    | expr ('<' | '>' | '<=' | '>=' | '=' | '!=') expr # operationExpr
    | ('not' | '!') expr                               # operationExpr
    | expr ('and' | '&') expr                          # operationExpr
    | expr ('or' | '|') expr                           # operationExpr
    | BOOL                                             # boolExpr
    | NUM                                              # numExpr
    | ID                                               # varExpr
    ;

BOOL : 'true' | 'false' ;                              // Boolean literals
ID : [a-z][a-zA-Z0-9_]* ;                              // Variable names
ID_FUNCTION : [A-Z][a-zA-Z0-9_]* ;                     // Function names
NUM : [0-9]+ ;                                         // Numbers
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;                // Block comments
LINE_COMMENT : '#' ~[\r\n]* '\r'? '\n' -> skip ;       // Line comments
WS : [ \n\r]+ -> skip ;                                // Whitespace