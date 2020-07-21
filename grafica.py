import sys
import ply.lex as lex
from LexProyecto import *
from YaccProyecto import *

import numpy as np

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPlainTextEdit, QSizePolicy, QPushButton


app = QApplication(sys.argv)

## labels de bienvenida
window = QWidget()
window.setWindowTitle('PROYECTO PRIMER PARCIAL')
window.setGeometry(300,300,400,600)
window.setStyleSheet("background-color: BEIGE;")
window.move(500,15)
saludo = QLabel('<h2>BIENVENIDO</h2>', parent= window)
labelRuta = QLabel('<h3>Escriba la sentencia a analizar: </h3>', parent = window)
saludo.move(60,15)
labelRuta.move(60,50)

## cuadro de texto
codigo = QPlainTextEdit(parent = window)
policy1 = codigo.sizePolicy()
policy1.setHorizontalPolicy(QSizePolicy.Expanding)
codigo.setSizePolicy(policy1)
codigo.setStyleSheet("background-color: HONEYDEW")
codigo.move(60,80)

## creacion de botones
botonSintactico = QPushButton(parent = window)
botonSintactico.setText("Sintáctico")
botonSintactico.setStyleSheet("background-color: LIGHTGRAY")
policy3 = botonSintactico.sizePolicy()
policy3.setHorizontalPolicy(QSizePolicy.Expanding)
botonSintactico.setSizePolicy(policy3)
botonSintactico.move(100,300)
botonLexer = QPushButton(parent = window)
botonLexer.setText("Lexico")
botonLexer.setStyleSheet("background-color: LIGHTGRAY")
policy4 = botonSintactico.sizePolicy()
policy4.setHorizontalPolicy(QSizePolicy.Expanding)
botonLexer.setSizePolicy(policy4)
botonLexer.move(205,300)

botonClear = QPushButton(parent = window)
botonClear.setText("Limpiar")
policy6= botonClear.sizePolicy()
policy6.setHorizontalPolicy(QSizePolicy.Expanding)
botonClear.setSizePolicy(policy6)
botonClear.move(300,15)





## cracion de box donde se recibe el resultado
resultado = QPlainTextEdit(parent = window)
policy5 = resultado.sizePolicy()
policy5.setHorizontalPolicy(QSizePolicy.Expanding)
resultado.setSizePolicy(policy5)
resultado.setStyleSheet("background-color: white")
resultado.move(60,350)



## funcion para darle funcionalidad al lexico


def analisisL():
    text = codigo.toPlainText()
    resultado.clear()
    analizador = lex.lex()
    analizador.input(text)

    while True:
        tokenRec = analizador.token()
        if tokenRec != None:
            resultado.appendPlainText(str(tokenRec))
            print(tokenRec)
        else:
            break

botonLexer.clicked.connect(analisisL)


def limpiar():
    codigo.setPlainText("")
    resultado.setPlainText("")

botonClear.clicked.connect(limpiar)

## funcion para darle funcionalidad al lexico
def analisisS():

    text = codigo.toPlainText()
    resultado.clear()
    parser = sintaxis.yacc()
    s = text
    arreglo=text.splitlines()

    """result = parser.parse(s)
    print(result)"""

    for x in arreglo:
        result = parser.parse(x)
        print(result)
        resultado.appendPlainText(str(result))



    #print('sdasdasd',resultado)


botonSintactico.clicked.connect(analisisS)


## METODOS PARA MOSTRAR
window.show()

sys.exit(app.exec_())