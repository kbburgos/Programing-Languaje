#Autor: Capobu
#Integrantes: Karla Burgos, Damian Castillo, Christian Portilla
#Paralelo: 2

#Analizador lexico JavaScript

import ply.lex as lex

#Definir todos los tokens para palabras reservadas.
reservadas = {
    'if'             : 'IF',
    'else'           : 'ELSE',
    'while'          : 'WHILE',
    'for'            : 'FOR',
    'console'        : 'CONSOLE',
    'prompt'         : 'PROMPT',
    'include'        : 'INCLUDE',
    'valueOf'        : 'VALUEOF',
    'chartAt'        : 'CHARTAT',
    'push'           : 'PUSH',
    'sort'           : 'SORT',
    'copyWithing'    : 'COPYWHITIN',
    'new'            : 'NEW',
    'slice'          : 'SLICE',
    'set'            : 'SET',
    'concat'         : 'CONCAT',
}

tokens = [ 'MENOS', 'MAS', 'PRODUCTO', 'DIVISION', 'NUMERO', 'LPAREN', 'RPAREN', 'IGUAL', 'COMA', 'COMILLA', 'PUNTO',
           'LCORCHETE', 'RCORCHETE', 'AND', 'OR', 'NOT', 'DIFERENTE', 'ASIGNACION', 'POTENCIA', 'FLOTANTE',
           'LISTA', 'STRING', 'BOOLEANO', 'OBJETO', 'PALABRA'] + list(reservadas.values())




#Simbolos matematicos y Operadores logicos
t_PUNTO=r'\.'
t_COMILLA=r'\"'
t_MENOS =r'\-'
t_MAS =r'\+'
t_PRODUCTO =r'\*'
t_DIVISION =r'/'
t_NUMERO=r'[0-9]+'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_IGUAL =r'==='
t_POTENCIA =r'\*\*'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_COMA = r'\,'
t_AND = r'&&'
t_OR = r'\|\|'
t_DIFERENTE = r'!='
t_ASIGNACION = r'='
#t_PALABRA= r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IF = r'if'
t_NOT =r'\!'
#t_FLOTANTE=r'[0-9]+.{1}[0-9]+'
#t_CADENA=r'\'[\w\s\W]*\''
#t_LISTA=r'\[[\w\s\W,?]*\]'
#t_PALABRA = r'[a-z$_][a-zA-Z0-9_]*'
t_OBJETO= r'\{[\w\s\W,?]*:{1}[\w\s\W,?]*\}'
t_FOR      = r'for'
t_WHILE    = r'while'
t_ELSE     = r'else'
t_ignore   = ' \t'
t_NEW      = r'new'
t_SET      = r'set'
t_STRING = r'".*?"'


def t_LISTA(t):
    r'(\[)((\[)?(([+-]?[0-9]+|\,)+|(("?\w*?"?)+|\,)+|([+-]?[0-9]+((\.[0-9]+))?|\,)+)(\]?))+(\,?)(\])'
    return t


def t_FLOTANTE(t):
    r'[-+]?[0-9]+((\.[0-9]+))?$'
    t.value = float(t.value)
    return t


def t_BOOLEAN(t):
    r'(True|False)'
    t.value = True if t.value == 'True' else False
    return t

def t_PALABRA(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'PALABRA')
    return t

def t_error(t):
    print("No se ha reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'

def t_CONSOLE(t):
    r'console.log'
    t.type = reservadas.get(t.value, 'CONSOLE')
    return t

def t_PROMPT(t):
    r'prompt'
    t.type = reservadas.get(t.value, 'PROMPT')
    return t

def t_INCLUDE(t):
    r'include'
    t.type = reservadas.get(t.value, 'INCLUDE')
    return t

def t_VALUEOF(t):
    r'valueOf'
    t.type = reservadas.get(t.value, 'VALUEOF')
    return t

def t_CHARTAT(t):
    r'[\.]chartAt'
    t.type = reservadas.get(t.value, 'CHARTAT')
    return t

def t_PUSH(t):
    r'[\.]push'
    t.type = reservadas.get(t.value, 'PUSH')
    return t

def t_SORT(t):
    r'[\.]sort'
    t.type = reservadas.get(t.value, 'SORT')
    return t

def t_COPYWITHING(t):
    r'[\.]copyWithing'
    t.type = reservadas.get(t.value, 'COPYWITHING')
    return t

def t_SLICE(t):
    r'[\.]slice'
    t.type = reservadas.get(t.value, 'SLICE')
    return t


def prueba(cadena):
    analizadorS= lex.lex()
    analizadorS.input(cadena)

    while True:
        tokenRec = analizadorS.token()
        if tokenRec!=None:
            print(tokenRec)
        else:
            break    
    
    

print('\nTest 1\n')
entradas = ['if', 'else', 'while', 'for',
            'variable.sort()',
            'variable.include(word)',
            'variable.slice(1,4)',
            'variable.push(word)',
            'variable.chartAt(3)',
            'console.log(word)',
            'prompt(word)',
            'variable.valueOf()']

for i in entradas:
    prueba(i)



print("\n\nSlice Permitido\n")

#slicePermitido
cadenaSlice = '"hello brother".slice(3,1)\n variable.slice(1,4)'
prueba(cadenaSlice)



print("\n\nInclude Permitido\n")

#includePermitido
cadenaInclude = '"hello brother".include("word")\n variable.include("word")\n "hello world".include(word)'
prueba(cadenaInclude)


print("\n\nPush Permitido\n")

#pushPermitido
cadenaPush = 'variable.push("word")\n world.push(word)'
prueba(cadenaPush)

#Operadores Matematicos y logicos
cadenaoperdores =[ '+', '-','*','/', '**', '&&', '||', '!', '!=', '=', '===']

for i in cadenaoperdores:
    prueba(i)

print('\n')

prueba('55===55\n')

prueba('10 != 1') #FLOTANTO NO RECONOCE

print ("4 EJEMPLOS")
entradas = ['listaNumeros= [1,2,3,4]',
            'objetoCarro={"marca" : "ford"}',
            'booleano = true', #TRUE NO RECONOCE
            'cadena = "soy una cadena de texto y nUMER02"'
            ]
for i in entradas:
    prueba(i)
