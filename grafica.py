import sys
import ply.lex as lex
from LexProyecto import *
from YaccProyecto import *


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPlainTextEdit, QSizePolicy, QPushButton


app = QApplication(sys.argv)

## labels de bienvenida
window = QWidget()
window.setWindowTitle('PROYECTO PRIMER PARCIAL')
window.setGeometry(3000,3000,600,750  )
window.move(60,15)
saludo = QLabel('<h2>BIENVENIDO</h2>', parent= window)
labelRuta = QLabel('<h3>Escriba la sentencia a analizar: </h3>', parent = window)
saludo.move(60,15)
labelRuta.move(60,50)

## cuadro de texto
codigo = QPlainTextEdit(parent = window)
policy1 = codigo.sizePolicy()
policy1.setHorizontalPolicy(QSizePolicy.Expanding)
codigo.setSizePolicy(policy1)
codigo.move(60,80)

## creacion de botones

botonSintactico = QPushButton(parent = window)
botonSintactico.setText("Sintáctico")
policy3 = botonSintactico.sizePolicy()
policy3.setHorizontalPolicy(QSizePolicy.Expanding)
botonSintactico.setSizePolicy(policy3)
botonSintactico.move(80,300)
botonLexer = QPushButton(parent = window)
botonLexer.setText("Lexico")
policy4 = botonSintactico.sizePolicy()
policy4.setHorizontalPolicy(QSizePolicy.Expanding)
botonLexer.setSizePolicy(policy4)
botonLexer.move(200,300)

## cracion de box donde se recibe el resultado
resultado = QPlainTextEdit(parent = window)
policy5 = resultado.sizePolicy()
policy5.setHorizontalPolicy(QSizePolicy.Expanding)
resultado.setSizePolicy(policy5)
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


## funcion para darle funcionalidad al lexico

def analisisS():
    text = codigo.toPlainText()
    resultado.clear()
    parser = sintaxis.yacc()


    s = text
    #except EOFError:
        
    result = parser.parse(s)
    resultado.appendPlainText(result)
    print(result)


botonSintactico.clicked.connect(analisisS)




## METODOS PARA MOSTRAR
window.show()

sys.exit(app.exec_())