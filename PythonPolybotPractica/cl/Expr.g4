grammar Expr;
root : COMMENT |expr (COMMENT)? EOF | command (COMMENT)? EOF ;
command : AREA expr
    | VERT expr
    | CENTER expr
    | PERI expr
    | PRINT expr
    | PRINT TEXT
    | DRAW IMGTEXT (', ') expr((', ') expr)*
    | COLOR expr(', ')COLORVAL
    | INSIDE expr(', ')expr
    | EQUAL expr(', ')expr
    | POLYGON (':=') expr
    ;
expr : '('expr')'
    | LISTOFPOINTS
    | expr INTERSEC expr
    | expr UNION expr
    | BOUNDINGBOX expr
    | EXCL NUM
    | POLYGON
    ;


NUM : [0-9]+;
COORD : (('-')?('0'..'9')+('.'('0'..'9')*)?);
COLOR : 'color';
COLCOORD : '0'('.'('0'..'9')*)?| ('1')('.'('0')*)?;
COLORVAL : '{'COLCOORD' 'COLCOORD' 'COLCOORD'}';
POINT : COORD' 'COORD;
LISTOFPOINTS : '['(POINT)?']' | '['(POINT)(('  ')POINT)*']';
CENTER : 'centroid';
VERT : 'vertices';
PERI : 'perimeter';
AREA : 'area';
DRAW : 'draw';
PRINT : 'print';
INSIDE : 'inside';
EQUAL : 'equal';
UNION : '+';
INTERSEC : '*';
BOUNDINGBOX : '#';
EXCL : '!';
POLYGON : [a-zA-Z_0-9]+ ;
COMMENT : '//'.*;
TEXT : '"'[-_a-zA-Z0-9(' ')]+'"';
IMGTEXT : '"'[.-_a-zA-Z0-9(' ')]+'"';
WS : [ \n]+ -> skip ;
