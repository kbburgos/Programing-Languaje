
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASCENDER ASIGNACION BOOLEANO CHARTAT COMA CONCAT CONSOLE DESCENDER DIFERENTE DIVISION ELSE FLOTANTE FOR IF IGUAL INCLUDE LISTA LLLAVES LOG LPAREN MAS MAYOR MENOR MENOS NEW NEWLINE NOT NUMERO OBJETO OR PALABRA POP POTENCIA PRODUCTO PROMPT PUNTO PUNTOCOMA PUSH RLLAVES RPAREN SET SLICE SORT STRING VALUEOF VAR WHILEsentencias : asignacion\n    | expresion\n    | metodos\n    | NEWLINE\n    sentencias : if\n    | while\n    | for\n    | sort\n    | include\n    | valueOf\n    | chartAt\n    | push\n    | slice\n    | pop\n    | concatmetodos : imprimirimprimir : PROMPT LPAREN factor RPARENimprimir : CONSOLE PUNTO LOG LPAREN factor RPARENif : IF LPAREN condicion RPAREN then\n    | IF LPAREN condicion RPAREN then else\n    else : ELSE thenwhile : WHILE LPAREN condicion RPAREN thenfor : FOR LPAREN VAR condicion PUNTOCOMA condicion PUNTOCOMA instruccion RPAREN thensort : LISTA SORTinclude : factor INCLUDE LPAREN factor RPARENvalueOf : factor VALUEOFchartAt : factor CHARTAT LPAREN factor RPARENpush : factor PUSH LPAREN factor RPARENslice : factor SLICE LPAREN factor COMA factor RPARENpop : factor POP concat : factor CONCAT LPAREN factor RPARENinstruccion : factor ASCENDER\n    | factor DESCENDERthen : LLLAVES sentencias RLLAVESasignacion : VAR PALABRA ASIGNACION sentencias\n    | PALABRA ASIGNACION sentenciasexpresion : term MAS factorexpresion : term MENOS factorexpresion : termexpresion : expresion PRODUCTO termexpresion : expresion DIVISION termexpresion : expresion POTENCIA termexpresion : term MAYOR factorexpresion : term MENOR factorcondicion : factor IGUAL factor\n    | factor MAYOR factor\n    | factor MENOR factor\n    | factor ASIGNACION factor\n    | NOT factor\n    | factor DIFERENTE factor\n    | compuesta AND condicion\n    | compuesta OR condicion\n    | compuesta\n    compuesta : LPAREN condicion RPARENterm : factorfactor : NEW SET LPAREN LISTA RPARENfactor : NUMEROfactor : FLOTANTEfactor : PALABRAfactor : STRINGfactor : LPAREN expresion RPARENfactor : LISTAfactor : BOOLEANOfactor : OBJETO'
    
_lr_action_items = {'NEWLINE':([0,39,65,116,],[5,5,5,5,]),'VAR':([0,39,57,65,116,],[17,17,83,17,17,]),'PALABRA':([0,17,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[18,38,55,55,55,55,18,55,55,55,55,55,55,55,18,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,18,55,55,]),'IF':([0,39,65,116,],[22,22,22,22,]),'WHILE':([0,39,65,116,],[24,24,24,24,]),'FOR':([0,39,65,116,],[25,25,25,25,]),'LISTA':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,86,96,97,98,99,100,102,103,107,112,116,125,137,],[26,54,54,54,54,26,54,54,54,54,54,54,54,26,54,54,54,54,54,54,54,54,108,54,54,54,54,54,54,54,54,54,26,54,54,]),'PROMPT':([0,39,65,116,],[27,27,27,27,]),'CONSOLE':([0,39,65,116,],[28,28,28,28,]),'NEW':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NUMERO':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'FLOTANTE':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'STRING':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'LPAREN':([0,22,23,24,25,27,35,36,37,39,40,41,42,43,44,46,47,48,50,51,56,59,61,65,71,72,73,74,75,76,79,83,85,96,97,98,99,100,102,103,107,112,116,125,137,],[23,51,23,56,57,59,23,23,23,23,23,23,23,23,71,72,73,74,75,76,76,23,86,23,23,23,23,23,23,76,23,76,107,23,23,23,23,23,76,76,23,23,23,76,23,]),'BOOLEANO':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'OBJETO':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,26,30,31,32,33,34,45,49,53,54,55,58,62,63,64,66,67,68,69,70,81,87,106,109,110,111,113,115,124,127,129,133,134,135,136,143,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-59,-39,-55,-16,-62,-57,-58,-60,-63,-64,-26,-30,-55,-62,-59,-24,-40,-41,-42,-36,-37,-38,-43,-44,-61,-35,-17,-25,-27,-28,-31,-19,-22,-56,-20,-18,-29,-21,-34,-23,]),'RLLAVES':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,26,30,31,32,33,34,45,49,53,54,55,58,62,63,64,66,67,68,69,70,81,87,106,109,110,111,113,115,124,127,129,131,133,134,135,136,143,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-59,-39,-55,-16,-62,-57,-58,-60,-63,-64,-26,-30,-55,-62,-59,-24,-40,-41,-42,-36,-37,-38,-43,-44,-61,-35,-17,-25,-27,-28,-31,-19,-22,-56,-20,136,-18,-29,-21,-34,-23,]),'PRODUCTO':([3,18,19,20,26,30,31,32,33,34,52,53,54,55,62,63,64,67,68,69,70,81,94,127,],[35,-59,-39,-55,-62,-57,-58,-60,-63,-64,35,-55,-62,-59,-40,-41,-42,-37,-38,-43,-44,-61,-55,-56,]),'DIVISION':([3,18,19,20,26,30,31,32,33,34,52,53,54,55,62,63,64,67,68,69,70,81,94,127,],[36,-59,-39,-55,-62,-57,-58,-60,-63,-64,36,-55,-62,-59,-40,-41,-42,-37,-38,-43,-44,-61,-55,-56,]),'POTENCIA':([3,18,19,20,26,30,31,32,33,34,52,53,54,55,62,63,64,67,68,69,70,81,94,127,],[37,-59,-39,-55,-62,-57,-58,-60,-63,-64,37,-55,-62,-59,-40,-41,-42,-37,-38,-43,-44,-61,-55,-56,]),'ASIGNACION':([18,30,31,32,33,34,38,54,55,78,81,94,127,],[39,-57,-58,-60,-63,-64,65,-62,-59,99,-61,99,-56,]),'INCLUDE':([18,20,26,30,31,32,33,34,81,127,],[-59,44,-62,-57,-58,-60,-63,-64,-61,-56,]),'VALUEOF':([18,20,26,30,31,32,33,34,81,127,],[-59,45,-62,-57,-58,-60,-63,-64,-61,-56,]),'CHARTAT':([18,20,26,30,31,32,33,34,81,127,],[-59,46,-62,-57,-58,-60,-63,-64,-61,-56,]),'PUSH':([18,20,26,30,31,32,33,34,81,127,],[-59,47,-62,-57,-58,-60,-63,-64,-61,-56,]),'SLICE':([18,20,26,30,31,32,33,34,81,127,],[-59,48,-62,-57,-58,-60,-63,-64,-61,-56,]),'POP':([18,20,26,30,31,32,33,34,81,127,],[-59,49,-62,-57,-58,-60,-63,-64,-61,-56,]),'CONCAT':([18,20,26,30,31,32,33,34,81,127,],[-59,50,-62,-57,-58,-60,-63,-64,-61,-56,]),'MAS':([18,19,20,26,30,31,32,33,34,53,54,55,81,94,127,],[-59,40,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,-61,-55,-56,]),'MENOS':([18,19,20,26,30,31,32,33,34,53,54,55,81,94,127,],[-59,41,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,-61,-55,-56,]),'MAYOR':([18,19,20,26,30,31,32,33,34,53,54,55,78,81,94,127,],[-59,42,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,97,-61,97,-56,]),'MENOR':([18,19,20,26,30,31,32,33,34,53,54,55,78,81,94,127,],[-59,43,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,98,-61,98,-56,]),'RPAREN':([19,30,31,32,33,34,52,53,54,55,62,63,64,67,68,69,70,77,80,81,82,84,88,89,90,92,93,94,101,108,114,117,118,119,120,121,122,123,126,127,128,138,141,142,],[-39,-57,-58,-60,-63,-64,81,-55,-62,-59,-40,-41,-42,-37,-38,-43,-44,95,-53,-61,104,106,109,110,111,113,114,-55,-49,127,-54,-45,-46,-47,-48,-50,-51,-52,133,-56,134,140,-32,-33,]),'SORT':([26,],[58,]),'PUNTO':([28,],[60,]),'SET':([29,],[61,]),'IGUAL':([30,31,32,33,34,54,55,78,81,94,127,],[-57,-58,-60,-63,-64,-62,-59,96,-61,96,-56,]),'DIFERENTE':([30,31,32,33,34,54,55,78,81,94,127,],[-57,-58,-60,-63,-64,-62,-59,100,-61,100,-56,]),'COMA':([30,31,32,33,34,54,55,81,91,127,],[-57,-58,-60,-63,-64,-62,-59,-61,112,-56,]),'PUNTOCOMA':([30,31,32,33,34,54,55,80,81,101,105,114,117,118,119,120,121,122,123,127,132,],[-57,-58,-60,-63,-64,-62,-59,-53,-61,-49,125,-54,-45,-46,-47,-48,-50,-51,-52,-56,137,]),'ASCENDER':([30,31,32,33,34,54,55,81,127,139,],[-57,-58,-60,-63,-64,-62,-59,-61,-56,141,]),'DESCENDER':([30,31,32,33,34,54,55,81,127,139,],[-57,-58,-60,-63,-64,-62,-59,-61,-56,142,]),'NOT':([51,56,76,83,102,103,125,],[79,79,79,79,79,79,79,]),'LOG':([60,],[85,]),'AND':([80,114,],[102,-54,]),'OR':([80,114,],[103,-54,]),'LLLAVES':([95,104,130,140,],[116,116,116,116,]),'ELSE':([115,136,],[130,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,39,65,116,],[1,66,87,131,]),'asignacion':([0,39,65,116,],[2,2,2,2,]),'expresion':([0,23,39,65,76,116,],[3,52,3,3,52,3,]),'metodos':([0,39,65,116,],[4,4,4,4,]),'if':([0,39,65,116,],[6,6,6,6,]),'while':([0,39,65,116,],[7,7,7,7,]),'for':([0,39,65,116,],[8,8,8,8,]),'sort':([0,39,65,116,],[9,9,9,9,]),'include':([0,39,65,116,],[10,10,10,10,]),'valueOf':([0,39,65,116,],[11,11,11,11,]),'chartAt':([0,39,65,116,],[12,12,12,12,]),'push':([0,39,65,116,],[13,13,13,13,]),'slice':([0,39,65,116,],[14,14,14,14,]),'pop':([0,39,65,116,],[15,15,15,15,]),'concat':([0,39,65,116,],[16,16,16,16,]),'term':([0,23,35,36,37,39,65,76,116,],[19,19,62,63,64,19,19,19,19,]),'factor':([0,23,35,36,37,39,40,41,42,43,51,56,59,65,71,72,73,74,75,76,79,83,96,97,98,99,100,102,103,107,112,116,125,137,],[20,53,53,53,53,20,67,68,69,70,78,78,84,20,88,89,90,91,92,94,101,78,117,118,119,120,121,78,78,126,128,20,78,139,]),'imprimir':([0,39,65,116,],[21,21,21,21,]),'condicion':([51,56,76,83,102,103,125,],[77,82,93,105,122,123,132,]),'compuesta':([51,56,76,83,102,103,125,],[80,80,80,80,80,80,80,]),'then':([95,104,130,140,],[115,124,135,143,]),'else':([115,],[129,]),'instruccion':([137,],[138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> asignacion','sentencias',1,'p_sentencias','YaccProyecto.py',7),
  ('sentencias -> expresion','sentencias',1,'p_sentencias','YaccProyecto.py',8),
  ('sentencias -> metodos','sentencias',1,'p_sentencias','YaccProyecto.py',9),
  ('sentencias -> NEWLINE','sentencias',1,'p_sentencias','YaccProyecto.py',10),
  ('sentencias -> if','sentencias',1,'p_sentencias_control','YaccProyecto.py',17),
  ('sentencias -> while','sentencias',1,'p_sentencias_control','YaccProyecto.py',18),
  ('sentencias -> for','sentencias',1,'p_sentencias_control','YaccProyecto.py',19),
  ('sentencias -> sort','sentencias',1,'p_sentencias_control','YaccProyecto.py',20),
  ('sentencias -> include','sentencias',1,'p_sentencias_control','YaccProyecto.py',21),
  ('sentencias -> valueOf','sentencias',1,'p_sentencias_control','YaccProyecto.py',22),
  ('sentencias -> chartAt','sentencias',1,'p_sentencias_control','YaccProyecto.py',23),
  ('sentencias -> push','sentencias',1,'p_sentencias_control','YaccProyecto.py',24),
  ('sentencias -> slice','sentencias',1,'p_sentencias_control','YaccProyecto.py',25),
  ('sentencias -> pop','sentencias',1,'p_sentencias_control','YaccProyecto.py',26),
  ('sentencias -> concat','sentencias',1,'p_sentencias_control','YaccProyecto.py',27),
  ('metodos -> imprimir','metodos',1,'p_metodos','YaccProyecto.py',32),
  ('imprimir -> PROMPT LPAREN factor RPAREN','imprimir',4,'p_imprimir','YaccProyecto.py',37),
  ('imprimir -> CONSOLE PUNTO LOG LPAREN factor RPAREN','imprimir',6,'p_imprimir_consola','YaccProyecto.py',42),
  ('if -> IF LPAREN condicion RPAREN then','if',5,'p_if','YaccProyecto.py',46),
  ('if -> IF LPAREN condicion RPAREN then else','if',6,'p_if','YaccProyecto.py',47),
  ('else -> ELSE then','else',2,'p_else','YaccProyecto.py',53),
  ('while -> WHILE LPAREN condicion RPAREN then','while',5,'p_while','YaccProyecto.py',57),
  ('for -> FOR LPAREN VAR condicion PUNTOCOMA condicion PUNTOCOMA instruccion RPAREN then','for',10,'p_for','YaccProyecto.py',62),
  ('sort -> LISTA SORT','sort',2,'p_sort','YaccProyecto.py',67),
  ('include -> factor INCLUDE LPAREN factor RPAREN','include',5,'p_include','YaccProyecto.py',72),
  ('valueOf -> factor VALUEOF','valueOf',2,'p_valueOf','YaccProyecto.py',77),
  ('chartAt -> factor CHARTAT LPAREN factor RPAREN','chartAt',5,'p_charAt','YaccProyecto.py',82),
  ('push -> factor PUSH LPAREN factor RPAREN','push',5,'p_push','YaccProyecto.py',87),
  ('slice -> factor SLICE LPAREN factor COMA factor RPAREN','slice',7,'p_slice','YaccProyecto.py',92),
  ('pop -> factor POP','pop',2,'p_pop','YaccProyecto.py',97),
  ('concat -> factor CONCAT LPAREN factor RPAREN','concat',5,'p_concat','YaccProyecto.py',102),
  ('instruccion -> factor ASCENDER','instruccion',2,'p_instruccion','YaccProyecto.py',107),
  ('instruccion -> factor DESCENDER','instruccion',2,'p_instruccion','YaccProyecto.py',108),
  ('then -> LLLAVES sentencias RLLAVES','then',3,'p_then','YaccProyecto.py',112),
  ('asignacion -> VAR PALABRA ASIGNACION sentencias','asignacion',4,'p_asignacion','YaccProyecto.py',117),
  ('asignacion -> PALABRA ASIGNACION sentencias','asignacion',3,'p_asignacion','YaccProyecto.py',118),
  ('expresion -> term MAS factor','expresion',3,'p_expresion_suma','YaccProyecto.py',124),
  ('expresion -> term MENOS factor','expresion',3,'p_expresion_resta','YaccProyecto.py',130),
  ('expresion -> term','expresion',1,'p_expression_term','YaccProyecto.py',135),
  ('expresion -> expresion PRODUCTO term','expresion',3,'p_expresion_producto','YaccProyecto.py',140),
  ('expresion -> expresion DIVISION term','expresion',3,'p_expresion_division','YaccProyecto.py',145),
  ('expresion -> expresion POTENCIA term','expresion',3,'p_expresion_potencia','YaccProyecto.py',150),
  ('expresion -> term MAYOR factor','expresion',3,'p_expresion_mayor','YaccProyecto.py',155),
  ('expresion -> term MENOR factor','expresion',3,'p_expresion_menor','YaccProyecto.py',160),
  ('condicion -> factor IGUAL factor','condicion',3,'p_condicion','YaccProyecto.py',166),
  ('condicion -> factor MAYOR factor','condicion',3,'p_condicion','YaccProyecto.py',167),
  ('condicion -> factor MENOR factor','condicion',3,'p_condicion','YaccProyecto.py',168),
  ('condicion -> factor ASIGNACION factor','condicion',3,'p_condicion','YaccProyecto.py',169),
  ('condicion -> NOT factor','condicion',2,'p_condicion','YaccProyecto.py',170),
  ('condicion -> factor DIFERENTE factor','condicion',3,'p_condicion','YaccProyecto.py',171),
  ('condicion -> compuesta AND condicion','condicion',3,'p_condicion','YaccProyecto.py',172),
  ('condicion -> compuesta OR condicion','condicion',3,'p_condicion','YaccProyecto.py',173),
  ('condicion -> compuesta','condicion',1,'p_condicion','YaccProyecto.py',174),
  ('compuesta -> LPAREN condicion RPAREN','compuesta',3,'p_compuesta','YaccProyecto.py',179),
  ('term -> factor','term',1,'p_term_factor','YaccProyecto.py',183),
  ('factor -> NEW SET LPAREN LISTA RPAREN','factor',5,'p_factor_set','YaccProyecto.py',188),
  ('factor -> NUMERO','factor',1,'p_factor_num','YaccProyecto.py',193),
  ('factor -> FLOTANTE','factor',1,'p_factor_flot','YaccProyecto.py',198),
  ('factor -> PALABRA','factor',1,'p_factor_pal','YaccProyecto.py',203),
  ('factor -> STRING','factor',1,'p_factor_str','YaccProyecto.py',208),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor_expr','YaccProyecto.py',213),
  ('factor -> LISTA','factor',1,'p_factor_lista','YaccProyecto.py',218),
  ('factor -> BOOLEANO','factor',1,'p_factor_booleano','YaccProyecto.py',223),
  ('factor -> OBJETO','factor',1,'p_factor_objeto','YaccProyecto.py',228),
]
