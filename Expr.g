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
    | <assoc=right> expr POW expr                  # powExpr
    | expr MUL expr                                # mulExpr
    | expr SUM expr                                # sumExpr
    | expr REL expr                                # relationalExpr
    | expr LOGIC expr                              # logicExpr
    | NOT expr                                     # notExpr
    | BOOL                                         # boolExpr
    | NUM                                          # numExpr
    | ID                                           # varExpr
    ;

POW : '^' ;                                        // Priority 1 binary operators
MUL : '*' | '/' | '%' ;                            // Priority 2 binary operators
SUM : '+' | '-' ;                                  // Priority 3 binary operators
REL : '<' | '>' | '<=' | '>=' | '==' | '!=' ;      // Priority 4 binary operators
LOGIC : 'and' | 'or' | 'xor' | '&&' | '||' ;       // Priority 5 binary operators

NOT : 'not' | '!' ;                                // Unary operator
BOOL : 'true' | 'false' ;                          // Boolean literals

ID : [a-z][a-zA-Z0-9_]* ;                          // Variable names
ID_FUNCTION : [A-Z][a-zA-Z0-9_]* ;                 // Function names
NUM : [0-9]+ ;                                     // Numbers
WS : [ \n]+ -> skip ;                              // Whitespace