grammar MyGrammer;

program : func_list ;

func_list : func_def func_list_prime ;

func_list_prime : func_list
          |
          ;

func_def : data_type ID '(' param_list ')' code_block ;

param_list : param param_list_prime
           |
           ;

param_list_prime : ',' param_list
           |
           ;

param : data_type ID ;

data_type : 'int' | 'double' | 'boolean' | 'void' ;

code_block : '{' stmt_list '}' ;

stmt_list : stmt stmt_list
          |  
          ;

decide : 'if' ;     

stmt : ';'
     | code_block
     | data_type var_list ';'
     | ID '=' expr ';'
     | ID '++' ';'
     | ID '--' ';'
     | 'return' stmt_return_prime
     | decide'(' expr ')' stmt stm_decide_prime
     | loop_stmt
     | expr ';'
     | init_stmt ';'
     ;

stmt_return_prime : ';'
                  |  expr ';'
                  ;

stm_decide_prime : ('else' stmt)?
                 |  
                 ;

loop : 'while' ;

loop_stmt : loop '(' expr ')' stmt ;

init_stmt : data_type ID '=' expr
          | ID '=' expr
          |
          ;

post_stmt : ID '=' expr
          | ID '++'
          | ID '--'
          |
          ;

var_list : var ',' var_list
         | var
         ;        

var : ID var_prime ;

var_prime : '=' expr
          |
          ;          

expr : number
     | ID
     | 'true'
     | 'false'
     | STRING_LIT
     | ID '(' args ')'
     | '(' expr ')' 
     |unop expr
     |expr binop expr
     ;

args : expr args_prime
     |
     ;

args_prime : ',' args
           |
           ;

unop : '-' | '!' ;

binop : ( '*' | '/' | '%' )
      | ( '+' | '-' )
      | ( '<' | '>' | '<=' | '>=' )
      | ( '==' | '!=' )
      | and
      | or
      ;

and : '&&' ;
or : '||';

number : INTEGER | DOUBLE;

Whitespace: [ \t]+ -> skip;
Newline: ( '\r' '\n'? | '\n') -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip;

INTEGER : '0' | [1-9] [0-9]*;
DOUBLE : INTEGER '.' ([0-9] | [e])+;
ID :  [a-zA-Z_] ([a-zA-Z_] | [0-9])*;
STRING_LIT : '"' ~('\r' | '\n' | '"' | '\\')* '"';


ERROR : . -> channel(HIDDEN);