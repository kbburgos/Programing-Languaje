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
    'var'            : 'VAR'
}

#indexación + and append

tokens = [ 'MENOS', 'MAS', 'PRODUCTO', 'DIVISION', 'NUMERO', 'LPAREN', 'RPAREN', 'IGUAL', 'POTENCIA', 'COMA',
'LCORCHETE', 'RCORCHETE', 'AND', 'OR', 'DIFERENTE', 'ASIGNACION' ] + list(reservadas.values())


#Simbolos matematicos
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
t_VAR = r'var'
t_IF       = r'if'
t_FOR      = r'for'
t_WHILE    = r'while'
t_ELSE     = r'else'
t_ignore   = ' \t'
t_NEW      = r'new'
t_SET      = r'set'




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
    r'[\.]include'
    t.type = reservadas.get(t.value, 'INCLUDE')
    return t

def t_VALUEOF(t):
    r'[\.]valueOf'
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




print('\nTest 1\n')
entradas = ['if', 'else', 'while', 'for'
            'variable.sort()',
            'variable.include(word)',
            'variable.slice(1,4)',
            'variable.push(word)',
            'variable.chartAt(3)',
            'console.log(word)',
            'prompt(word)',
            'variable.valueOf()']

for i in entradas:
    analizadorE = lex.lex()
    analizadorE.input(i)
    while True:
        tokenRec = analizadorE.token()
        if tokenRec != None:
            print(tokenRec)
        else:
            break



print("\n\nSlice Permitido\n")

#slicePermitido
cadenaSlice = '"hello brother".slice(3,1)\n variable.slice(1,4)'
analizadorS= lex.lex()
analizadorS.input(cadenaSlice)

while True:
    tokenRec = analizadorS.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break



print("\n\nInclude Permitido\n")

#includePermitido
cadenaInclude = '"hello brother".include("word")\n variable.include("word")\n "hello world".include(word)'
analizadorI= lex.lex()
analizadorI.input(cadenaInclude)

while True:
    tokenRec = analizadorI.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break



print("\n\nPush Permitido\n")

#pushPermitido
cadenaPush = 'variable.push("word")\n world.push(word)'
analizadorP= lex.lex()
analizadorP.input(cadenaPush)

while True:
    tokenRec = analizadorP.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break



#Definir todos los tokens para operadores y símbolos válidos.

#Definir tipo de datos y cómo se pueden escribir variables en su LP.

#Realizar pruebas para tokenizar sus componentes. Al menos 3 ejemplos de líneas válidas por cada integrante.

#Subir a sidweb su analizador lexico.py validado, los ejemplos comprobados, y su link del repositorio.
