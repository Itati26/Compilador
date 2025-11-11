grammar Grammar;

program:(statement NEWLINE)*EOF;

statement:assing|print|if_statement|for_statement;
/*Definimos la asignación*/
assing:ID'='expr;

/*Definimos print*/
print:'print''('expr')';

/*Definimos if */
if_statement:'if''('expr')'block;

/*Definimos for */
for_statement:'for''('assing';'expr';'assing')'block;

/*Definimos un bloque */
block:'{'(statement NEWLINE)*'}';

/*Definimos la expresión */
expr:expr op=('*'|'/')expr
    |expr op=('*'|'-')expr
    |expr op=('>'|'<'|'>='|'<=')expr
    |expr op=('=='|'!=')expr
    |ID
    |'('expr')'
    ;

/*Definir elementos finales */

ID:[a-zA-Z][a-z-A-Z_0-9]*;
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';

