grammar While;

/** starting rule for the program

*/
prog: stat (NEWLINE | EOF);

simple_stat
    : SK                                           # Skip
    | ID ':=' expr                                      # Assg
    | IF bexpr THEN simple_stat ELSE simple_stat    # IfThenElse
    | WHILE bexpr DO simple_stat                    # WhileDo
    | '{' stat '}'                                      # NestStat
    ;

stat: simple_stat ';' stat  # Seq
    | simple_stat           # SingleStat
    ;

expr: expr (MUL | DIV) expr # Mult
    | expr (ADD | SUB) expr # Add
    | INT                   # Int
    | ID                    # Id
    | '(' expr ')'          # NestExpr
    ;

bexpr
    : expr '<=' expr        # Lte
    | expr '=' expr         # Eq
    | expr '<' expr         # Lt
    | '\u00AC' bexpr             # Not
    | bexpr '\u2227' bexpr       # And
    | bexpr '\u2228' bexpr       # Or
    | TRUE                # True
    | FALSE               # False
    | '(' bexpr ')'         # NestBexpr
    ;

TRUE: 'true' ;
FALSE: 'false';
SK: 'skip' ;
IF: 'if' ;
THEN: 'then' ;
ELSE: 'else';
WHILE: 'while';
DO: 'do' ;

MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';

ID  :    [a-zA-Z][a-zA-Z0-9]*;
INT :    '-'?[0-9]+ ;
NEWLINE:'\r'? '\n';
WS  : [ \t]+ -> skip ;
