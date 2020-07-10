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
    'echo'           : 'ECHO',
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
    'set'            : 'SET'
}


tokens = ["MENOS","MAS", "PRODUCTO",
"DIVISION", "NUMERO", "LPAREN","RPAREN", "IGUAL", "POTENCIA", "AND", "OR", "NOT", 
"IGUAL2", "IGUAL3", "NOIGUAL"

] + list(reservadas.values())

#Simbolos matematicos y Operadores logicos
t_MENOS =r'\-'
t_MAS =r'\+'
t_PRODUCTO =r'\*'
t_DIVISION =r'/'
t_NUMERO=r'[0-9]+'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_IGUAL =r'='
t_POTENCIA =r'\*\*'
t_AND =r'&&'
t_OR = r'\|\|'
t_NOT =r'\!' 
t_IGUAL2 =r'\=\='
t_IGUAL3 =r'\=\=\='
t_NOIGUAL=r'\!\='



t_IF       = r'if'
t_FOR      = r'for'
t_WHILE    = r'while'
t_ELSE     = r'else'
t_ignore   = ' \t'
t_ECHO     = r'echo'
t_NEW      = r'new'
t_SET      = r'set'

def t_error(t):
    print("No se ha reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


def t_NEWLINE(t):
    r'\n+'


def t_CONSOLE(t):
    r'console.log\([\[\(]?("?.*?"?)+[\]\)]?\)'
    t.type = reservadas.get(t.value, 'CONSOLE')
    return t


def t_PROMPT(t):
    r'prompt\([\[\(]?("?.*?"?)+[\]\)]?\)'
    t.type = reservadas.get(t.value, 'PROMPT')
    return t


def t_INCLUDE(t):
    r'(((")[\w\s?]+")|[\w]+)[\.]include\((("[aA-zZ 0-9]+")|[aA-zZ 0-9]+)\)|(;$)'
    t.type = reservadas.get(t.value, 'INCLUDE')
    return t


def t_VALUEOF(t):
    r'(((")[\w\s?]+")|[\w]+)[\.]valueOf\(\)|(;$)'
    t.type = reservadas.get(t.value, 'VALUEOF')
    return t


def t_CHARTAT(t):
    r'(((")[\w\s?]+")|[\w]+)[\.]chartAt\(([0-9]+)\)|(;$)'
    t.type = reservadas.get(t.value, 'CHARTAT')
    return t



def t_PUSH(t):
    r'[\w]+[\.]push\((("[aA-zZ 0-9]+")|([aA-zZ 0-9]+))\)|(;$)'
    t.type = reservadas.get(t.value, 'PUSH')
    return t



def t_SORT(t):
    r'[\w]+[\.]sort\(\)|(;$)'
    t.type = reservadas.get(t.value, 'SORT')
    return t



def t_COPYWITHING(t):
    r'[\w]+[\.]copyWithing\((([\d]+,\s?[\d]+)|([\d]+,\s?[\d]+,\s?[\d]+))\)|(;$)'
    t.type = reservadas.get(t.value, 'COPYWITHING')
    return t



def t_SLICE(t):
    r'(((")[\w\s?]+")|[\w]+)[\.]slice\(([\d]+,\s?[\d]+)\)|(;$)'
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
cadenaoperdores =[ "+", '-','*','/', '**', '&&', '||', '!', '!=', '==', '===']

for i in cadenaoperdores:
    prueba(i)

print('\n')

prueba("55 ==55\n")

prueba('10 != 1')

#Definir todos los tokens para operadores y símbolos válidos.

#Definir tipo de datos y cómo se pueden escribir variables en su LP.

#Realizar pruebas para tokenizar sus componentes. Al menos 3 ejemplos de líneas válidas por cada integrante.

#Subir a sidweb su analizador lexico.py validado, los ejemplos comprobados, y su link del repositorio.
