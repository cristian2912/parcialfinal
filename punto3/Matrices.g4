grammar Matrices;

// ----------------------
// Regla inicial
// ----------------------
prog
    : declList stmtList EOF
    ;

// ----------------------
// Declaraciones
// Prog → DeclList StmtList
// DeclList → Decl DeclList | ε
// Decl → mat id '[' num ',' num ']' ';'
// ----------------------
declList
    : decl declList
    |               // vacío
    ;

decl
    : MAT ID '[' NUM ',' NUM ']' ';'
    ;

// ----------------------
// Sentencias
// StmtList → Stmt StmtList | ε
// Stmt     → Assign ';'
// Assign   → id '=' Expr
// ----------------------
stmtList
    : stmt stmtList
    |               // vacío
    ;

stmt
    : assign ';'
    ;

assign
    : ID '=' expr
    ;

// ----------------------
// Expresiones
// Expr   → Expr '+' Term | Expr '-' Term | Term
// Term   → Term '*' Factor | Factor
// Factor → id | '(' Expr ')'
// ----------------------
expr
    : expr '+' term
    | expr '-' term
    | term
    ;

term
    : term '*' factor
    | factor
    ;

factor
    : ID
    | '(' expr ')'
    ;

// ----------------------
// LÉXICO
// ----------------------
MAT : 'mat' ;

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;
NUM : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;

LBRACK : '[' ;
RBRACK : ']' ;
COMMA  : ',' ;
SEMI   : ';' ;
ASSIGN : '=' ;
PLUS   : '+' ;
MINUS  : '-' ;
STAR   : '*' ;
LPAREN : '(' ;
RPAREN : ')' ;
