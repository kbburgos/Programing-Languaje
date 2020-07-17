import ply.yacc as sintaxis
import LexProyecto
tokens = LexProyecto.tokens


def p_sentencias(p):
    '''sentencias : asignacion
    | expresion
    | metodos
    | then'''
    p[0] = p[1]


def p_sentencias_control(p):
    '''sentencias : if
    | while
    | for
    | sort
    | include
    | valueOf
    | chartAt
    | push
    | slice
    | pop
    | concat'''
    p[0] = p[1]


def p_metodos(p):
    'metodos : imprimir'
    p[0]=('IMPRIMIR')


def p_imprimir(p):
    'imprimir : PROMPT LPAREN factor RPAREN'


def p_imprimir_consola(p):
    '''imprimir : CONSOLE LPAREN factor RPAREN'''


def p_if(p):
    '''if : IF LPAREN condicion RPAREN sentencias
    | IF LPAREN condicion RPAREN sentencias else
    '''
    p[0]=('IF')


def p_else(p):
    'else : ELSE LLLAVES sentencias RLLAVES'


def p_while(p):
    'while : WHILE LPAREN condicion RPAREN sentencias'
    p[0] = ('WHILE')


def p_for(p):
    'for : FOR LPAREN VAR condicion PUNTOCOMA condicion PUNTOCOMA instruccion RPAREN'
    p[0] = ('FOR')


def p_sort(p):
    'sort : LISTA SORT'
    p[0]= ('SORT')


def p_include(p):
    'include : factor INCLUDE LPAREN factor RPAREN'
    p[0]= ('INCLUDE')


def p_valueOf(p):
    'valueOf : factor VALUEOF'
    p[0]= ('VALUEOF')


def p_charAt(p):
    'chartAt : factor CHARTAT LPAREN factor RPAREN'
    p[0]= ('CHARAT')


def p_push(p):
    'push : factor PUSH LPAREN factor RPAREN'
    p[0] = ('PUSH')


def p_slice(p):
    'slice : factor SLICE LPAREN factor COMA factor RPAREN'
    p[0] = ('SLICE')


def p_pop(p):
    'pop : factor POP '
    p[0] = ('POP')


def p_concat(p):
    'concat : factor CONCAT LPAREN factor RPAREN'
    p[0] = ('CONCAT')


def p_instruccion(p):
    '''instruccion : factor ASCENDER
    | factor DESCENDER'''


def p_then(p):
    'then : LLLAVES sentencias RLLAVES'


def p_asignacion(p):
    'asignacion : PALABRA ASIGNACION expresion'
    p[0] = ('ASIGNACION')


def p_expresion_suma(p):
    'expresion : term MAS factor'
    p[0] = p[1] + p[3]


def p_expresion_resta(p):
    'expresion : term MENOS factor'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expresion : term'
    p[0] = p[1]


def p_expresion_producto(p):
    'expresion : expresion PRODUCTO term'
    p[0] = p[1] * p[3]


def p_expresion_division(p):
    'expresion : expresion DIVISION term'
    p[0] = p[1] / p[3]


def p_expresion_potencia(p):
    'expresion : expresion POTENCIA term'
    p[0] = p[1] ** p[3]


#validar con expresiones
def p_condicion(p):
    '''condicion : factor IGUAL factor
    | factor MAYOR factor
    | factor MENOR factor
    | factor ASIGNACION factor
    | NOT factor
    | factor DIFERENTE factor
    | compuesta AND condicion
    | compuesta OR condicion
    | compuesta
    '''


def p_compuesta(p):
    '''compuesta : LPAREN condicion RPAREN'''


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_set(p):
    'factor : NEW SET LPAREN LISTA RPAREN'
    p[0]=('CONJUNTO')


def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]


def p_factor_flot(p):
    'factor : FLOTANTE'
    p[0] = p[1]


def p_factor_pal(p):
    'factor : PALABRA'
    p[0] = p[1]


def p_factor_str(p):
    'factor : STRING'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'
    p[0] = p[2]


def p_factor_lista(p):
    'factor : LISTA'
    p[0] = ('LISTA')


def p_factor_booleano(p):
    'factor : BOOLEANO'
    p[0] = ('BOOLEANO')


def p_factor_objeto (p):
    'factor : OBJETO'
    p[0] = ('OBJETO')


def p_error(p):
    print("Error de sintaxis:")


# Construir parser
parser = sintaxis.yacc()
while True:
    try:
        s = input('<JS?> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)




##ejemplos pobrar Christian Portilla
##CREACION DE UNA LISTA
## lista = ["hola","como","estas"]
##CREACION DE UN BOOLEANO
## booleano = true
## CREACION DE UN OBJETO
## carro= {"ford":"ranger"}
## CREACION DE UNA CADENA DE CARACTERES
## cadena = "hola soy un4 Cad3NA"

##ejemplos Damian Castillo
##suma = 4 + 5 + 89
##numero = 69
## 5 ===9
