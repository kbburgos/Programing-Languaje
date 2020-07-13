import ply.yacc as sintaxis
import LexProyecto
tokens = LexProyecto.tokens


def p_sentencias(p):
    '''sentencias : asignacion
    | expresion
    | metodos
    | if
    | PALABRA ASIGNACION FLOTANTE'''
    p[0] = p[1]


def p_metodos(p):
    '''metodos : imprimir
    '''


def p_imprimir(p):
    'imprimir : PROMPT factor'


def p_if(p):
    '''if : IF LPAREN condicion RPAREN LLLAVES sentencias RLLAVES
    '''


def p_else(p):
    'else : ELSE LLLAVES sentencias RLLAVES'


def p_asignacion(p):
    'asignacion : PALABRA ASIGNACION expresion'


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


def p_condicion(p):
    'condicion : factor IGUAL factor'


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]


def p_factor_str(p):
    'factor : STRING'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'
    p[0] = p[2]

def p_factor_lista(p):
    'factor : LISTA'

def p_factor_booleano(p):
    'factor : BOOLEANO'

def p_factor_objeto (p):
    'factor : OBJETO'

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
