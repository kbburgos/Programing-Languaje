# Autor: Capobu
# Integrantes: Karla Burgos, Damian Castillo, Christian Portilla
# Paralelo: 2

# Analizador lexico JavaScript

import ply.lex as lex

# Definir todos los tokens para palabras reservadas.
reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'console': 'CONSOLE',
    'prompt': 'PROMPT',
    'include': 'INCLUDE',
    'valueOf': 'VALUEOF',
    'chartAt': 'CHARTAT',
    'push': 'PUSH',
    'sort': 'SORT',
    'new': 'NEW',
    'slice': 'SLICE',
    'set': 'SET',
    'concat': 'CONCAT',
    'var' : 'VAR',
    'pop': 'POP',
}

tokens = ['MENOS', 'MAS', 'PRODUCTO', 'DIVISION', 'NUMERO', 'LPAREN', 'RPAREN', 'IGUAL', 'COMA','AND',
          'OR', 'NOT', 'DIFERENTE', 'ASIGNACION', 'POTENCIA', 'FLOTANTE',
          'LISTA', 'STRING', 'BOOLEANO', 'OBJETO', 'PALABRA', 'LLLAVES', 'RLLAVES', 'PUNTOCOMA', 'MAYOR',
          'MENOR', 'ASCENDER', 'DESCENDER', 'NEWLINE'] + list(reservadas.values())

# Simbolos matematicos y Operadores logicos
#t_PUNTO = r'\.'
t_MAYOR= r'\>'
t_MENOR= r'\<'
t_PUNTOCOMA = r'\;'
#t_COMILLA = r'\"'
t_MENOS = r'\-'
t_MAS = r'\+'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
# t_NUMERO=r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUAL = r'==='
t_POTENCIA = r'\*\*'
#t_LCORCHETE = r'\['
#t_RCORCHETE = r'\]'
t_LLLAVES = r'\{'
t_RLLAVES = r'\}'
t_COMA = r'\,'
t_AND = r'&&'
t_OR = r'\|\|'
t_DIFERENTE = r'!='
t_ASIGNACION = r'='
# t_PALABRA= r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IF = r'if'
t_NOT = r'\!'
# t_FLOTANTE=r'[0-9]+.{1}[0-9]+'
# t_CADENA=r'\'[\w\s\W]*\''
# t_LISTA=r'\[[\w\s\W,?]*\]'
# t_PALABRA = r'[a-z$_][a-zA-Z0-9_]*'
t_OBJETO = r'\{[\w\s\W,?]*:{1}[\w\s\W,?]*\}'
t_FOR = r'for'
t_WHILE = r'while'
t_ELSE = r'else'
t_ignore = ' \t'
t_NEW = r'new'
t_SET = r'set'
t_STRING = r'".*?"'
t_VAR = r'var'
t_ASCENDER=r'\+\+'
t_DESCENDER=r'\-\-'


def t_NUMERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_LISTA(t):
    r'(\[)((\[)?(([+-]?[0-9]+|\,)+|(("?\w*?"?)+|\,)+|([+-]?[0-9]+((\.[0-9]+))?|\,)+)(\]?))+(\,?)(\])'
    return t


def t_FLOTANTE(t):
    r'[-+]?[0-9]+(\.)[0-9]+'
    t.value = float(t.value)
    return t


def t_BOOLEANO(t):
    r'(true|false)'
    t.value = True if t.value == 'true' else False
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
    t.lexer.lineno += len(t.value)


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


def t_CONCAT(t):
    r'[\.]concat'
    t.type = reservadas.get(t.value, 'CONCAT')
    return t


def t_VALUEOF(t):
    r'[\.]valueOf\(\)'
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
    r'[\.]sort\(\)'
    t.type = reservadas.get(t.value, 'SORT')
    return t


def t_POP(t):
    r'[\.]pop\(\)'
    t.type = reservadas.get(t.value, 'POP')
    return t


def t_SLICE(t):
    r'[\.]slice'
    t.type = reservadas.get(t.value, 'SLICE')
    return t


print(
    "#################################################################################################################\n")
print(
    "#####################################          CAPOBU          ##################################################")
print("\nAnalizador Léxico JavaScript\nIntegrantes:\nKarla Burgos\nDamian Castillo\nChristian Portilla")
print(
    "\n#################################################################################################################\n")

print("KARLA BURGOS: EJERCICIOS VARIOS\n")

entradas = ['if', 'else', 'while', 'for',
            'variable.sort()',
            'variable.include(word)',
            'variable.slice(1,4)',
            'variable.push(word)',
            'variable.chartAt(3)',
            'console.log(word)',
            'prompt(word)',
            'arreglo.concat(arreglo)'
            'var variable=4',
            '5++']

analizadorP1 = lex.lex()
for i in entradas:
    analizadorP1.input(i)
    while True:
        tokenRec = analizadorP1.token()
        if tokenRec != None:
            print(tokenRec)
        else:
            break

print("\n")
cadenaSlice = '"hello brother".slice(3,1)\n variable.slice(1,4)'
analizadorP2 = lex.lex()
analizadorP2.input(cadenaSlice)
while True:
    tokenRec = analizadorP2.token()
    if tokenRec != None:
        print(tokenRec)
    else:
        break

print("\n")
cadenaInclude = '"hello brother".include("word")\n variable.include("word")\n "hello world".include(word)'
analizadorP3 = lex.lex()
analizadorP3.input(cadenaInclude)
while True:
    tokenRec = analizadorP3.token()
    if tokenRec != None:
        print(tokenRec)
    else:
        break

print("\nDAMIAN CASTILLO: EJERCICIOS VARIOS\n")
cadenaoperdores = ['+', '-', '*', '/', '**', '&&', '||', '!', '!=', '=', '===']
analizadorP4 = lex.lex()
for i in cadenaoperdores:
    analizadorP4.input(i)
    while True:
        tokenRec = analizadorP4.token()
        if tokenRec != None:
            print(tokenRec)
        else:
            break

print("\n")
igualdad = '55===55\n'
analizadorP6 = lex.lex()
analizadorP6.input(igualdad)
while True:
    tokenRec = analizadorP6.token()
    if tokenRec != None:
        print(tokenRec)
    else:
        break

print("\n")
desigualdad = '10 != 1'
analizadorP7 = lex.lex()
analizadorP7.input(desigualdad)
while True:
    tokenRec = analizadorP7.token()
    if tokenRec != None:
        print(tokenRec)
    else:
        break

print("\nCHRISTIAN PORTILLA: EJERCICIOS VARIOS\n")
ejercicio = ['listaNumeros= [1,2,3,4]',
             'objetoCarro={"marca" : "ford"}',
             'booleano = true',
             'cadena ="soy una cadena de texto y nUMER02"'
             'con = new Set (["a","b"])'
             ]
analizadorP5 = lex.lex()
for i in ejercicio:
    analizadorP5.input(i)
    while True:
        tokenRec = analizadorP5.token()
        if tokenRec != None:
            print(tokenRec)
        else:
            break