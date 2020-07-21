
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASCENDER ASIGNACION BOOLEANO CHARTAT COMA CONCAT CONSOLE DESCENDER DIFERENTE DIVISION ELSE FLOTANTE FOR IF IGUAL INCLUDE LISTA LLLAVES LOG LPAREN MAS MAYOR MENOR MENOS NEW NEWLINE NOT NUMERO OBJETO OR PALABRA POP POTENCIA PRODUCTO PROMPT PUNTO PUNTOCOMA PUSH RLLAVES RPAREN SET SLICE SORT STRING VALUEOF VAR WHILEsentencias : asignacion\n    | expresion\n    | metodos\n    | NEWLINE\n    sentencias : if\n    | while\n    | for\n    | sort\n    | include\n    | valueOf\n    | chartAt\n    | push\n    | slice\n    | pop\n    | concatmetodos : imprimirimprimir : PROMPT LPAREN factor RPARENimprimir : CONSOLE PUNTO LOG LPAREN factor RPARENif : IF LPAREN condicion RPAREN then\n    | IF LPAREN condicion RPAREN then else\n    else : ELSE thenwhile : WHILE LPAREN condicion RPAREN thenfor : FOR LPAREN VAR condicion PUNTOCOMA condicion PUNTOCOMA instruccion RPAREN thensort : LISTA SORTinclude : factor INCLUDE LPAREN factor RPARENvalueOf : factor VALUEOFchartAt : factor CHARTAT LPAREN factor RPARENpush : factor PUSH LPAREN factor RPARENslice : factor SLICE LPAREN factor COMA factor RPARENpop : factor POP concat : factor CONCAT LPAREN factor RPARENinstruccion : factor ASCENDER\n    | factor DESCENDERthen : LLLAVES sentencias RLLAVESasignacion : PALABRA ASIGNACION expresionexpresion : term MAS factorexpresion : term MENOS factorexpresion : termexpresion : expresion PRODUCTO termexpresion : expresion DIVISION termexpresion : expresion POTENCIA termexpresion : term MAYOR factorexpresion : term MENOR factorcondicion : factor IGUAL factor\n    | factor MAYOR factor\n    | factor MENOR factor\n    | factor ASIGNACION factor\n    | NOT factor\n    | factor DIFERENTE factor\n    | compuesta AND condicion\n    | compuesta OR condicion\n    | compuesta\n    | NEWLINE\n    compuesta : LPAREN condicion RPARENterm : factorfactor : NEW SET LPAREN LISTA RPARENfactor : NUMEROfactor : FLOTANTEfactor : PALABRAfactor : STRINGfactor : LPAREN expresion RPARENfactor : LISTAfactor : BOOLEANOfactor : OBJETO'
    
_lr_action_items = {'NEWLINE':([0,49,54,73,81,99,100,113,122,],[5,78,78,78,78,78,78,5,78,]),'PALABRA':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[17,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,17,53,53,]),'IF':([0,113,],[21,21,]),'WHILE':([0,113,],[23,23,]),'FOR':([0,113,],[24,24,]),'LISTA':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,84,93,94,95,96,97,99,100,104,109,113,122,134,],[25,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,105,52,52,52,52,52,52,52,52,52,25,52,52,]),'PROMPT':([0,113,],[26,26,]),'CONSOLE':([0,113,],[27,27,]),'NEW':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'NUMERO':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'FLOTANTE':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'LPAREN':([0,21,22,23,24,26,34,35,36,37,38,39,40,41,42,44,45,46,48,49,54,57,59,68,69,70,71,72,73,76,81,83,93,94,95,96,97,99,100,104,109,113,122,134,],[22,49,22,54,55,57,22,22,22,22,22,22,22,22,68,69,70,71,72,73,73,22,84,22,22,22,22,22,73,22,73,104,22,22,22,22,22,73,73,22,22,22,73,22,]),'BOOLEANO':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'OBJETO':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,29,30,31,32,33,43,47,51,52,53,56,60,61,62,63,64,65,66,67,79,103,106,107,108,110,112,121,124,126,130,131,132,133,140,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-59,-38,-55,-16,-62,-57,-58,-60,-63,-64,-26,-30,-55,-62,-59,-24,-39,-40,-41,-35,-36,-37,-42,-43,-61,-17,-25,-27,-28,-31,-19,-22,-56,-20,-18,-29,-21,-34,-23,]),'RLLAVES':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,29,30,31,32,33,43,47,51,52,53,56,60,61,62,63,64,65,66,67,79,103,106,107,108,110,112,121,124,126,128,130,131,132,133,140,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-59,-38,-55,-16,-62,-57,-58,-60,-63,-64,-26,-30,-55,-62,-59,-24,-39,-40,-41,-35,-36,-37,-42,-43,-61,-17,-25,-27,-28,-31,-19,-22,-56,-20,133,-18,-29,-21,-34,-23,]),'PRODUCTO':([3,17,18,19,25,29,30,31,32,33,50,51,52,53,60,61,62,63,64,65,66,67,79,91,124,],[34,-59,-38,-55,-62,-57,-58,-60,-63,-64,34,-55,-62,-59,-39,-40,-41,34,-36,-37,-42,-43,-61,-55,-56,]),'DIVISION':([3,17,18,19,25,29,30,31,32,33,50,51,52,53,60,61,62,63,64,65,66,67,79,91,124,],[35,-59,-38,-55,-62,-57,-58,-60,-63,-64,35,-55,-62,-59,-39,-40,-41,35,-36,-37,-42,-43,-61,-55,-56,]),'POTENCIA':([3,17,18,19,25,29,30,31,32,33,50,51,52,53,60,61,62,63,64,65,66,67,79,91,124,],[36,-59,-38,-55,-62,-57,-58,-60,-63,-64,36,-55,-62,-59,-39,-40,-41,36,-36,-37,-42,-43,-61,-55,-56,]),'ASIGNACION':([17,29,30,31,32,33,52,53,75,79,91,124,],[37,-57,-58,-60,-63,-64,-62,-59,96,-61,96,-56,]),'INCLUDE':([17,19,25,29,30,31,32,33,79,124,],[-59,42,-62,-57,-58,-60,-63,-64,-61,-56,]),'VALUEOF':([17,19,25,29,30,31,32,33,79,124,],[-59,43,-62,-57,-58,-60,-63,-64,-61,-56,]),'CHARTAT':([17,19,25,29,30,31,32,33,79,124,],[-59,44,-62,-57,-58,-60,-63,-64,-61,-56,]),'PUSH':([17,19,25,29,30,31,32,33,79,124,],[-59,45,-62,-57,-58,-60,-63,-64,-61,-56,]),'SLICE':([17,19,25,29,30,31,32,33,79,124,],[-59,46,-62,-57,-58,-60,-63,-64,-61,-56,]),'POP':([17,19,25,29,30,31,32,33,79,124,],[-59,47,-62,-57,-58,-60,-63,-64,-61,-56,]),'CONCAT':([17,19,25,29,30,31,32,33,79,124,],[-59,48,-62,-57,-58,-60,-63,-64,-61,-56,]),'MAS':([17,18,19,25,29,30,31,32,33,51,52,53,79,91,124,],[-59,38,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,-61,-55,-56,]),'MENOS':([17,18,19,25,29,30,31,32,33,51,52,53,79,91,124,],[-59,39,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,-61,-55,-56,]),'MAYOR':([17,18,19,25,29,30,31,32,33,51,52,53,75,79,91,124,],[-59,40,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,94,-61,94,-56,]),'MENOR':([17,18,19,25,29,30,31,32,33,51,52,53,75,79,91,124,],[-59,41,-55,-62,-57,-58,-60,-63,-64,-55,-62,-59,95,-61,95,-56,]),'RPAREN':([18,29,30,31,32,33,50,51,52,53,60,61,62,64,65,66,67,74,77,78,79,80,82,85,86,87,89,90,91,98,105,111,114,115,116,117,118,119,120,123,124,125,135,138,139,],[-38,-57,-58,-60,-63,-64,79,-55,-62,-59,-39,-40,-41,-36,-37,-42,-43,92,-52,-53,-61,101,103,106,107,108,110,111,-55,-48,124,-54,-44,-45,-46,-47,-49,-50,-51,130,-56,131,137,-32,-33,]),'SORT':([25,],[56,]),'PUNTO':([27,],[58,]),'SET':([28,],[59,]),'IGUAL':([29,30,31,32,33,52,53,75,79,91,124,],[-57,-58,-60,-63,-64,-62,-59,93,-61,93,-56,]),'DIFERENTE':([29,30,31,32,33,52,53,75,79,91,124,],[-57,-58,-60,-63,-64,-62,-59,97,-61,97,-56,]),'COMA':([29,30,31,32,33,52,53,79,88,124,],[-57,-58,-60,-63,-64,-62,-59,-61,109,-56,]),'PUNTOCOMA':([29,30,31,32,33,52,53,77,78,79,98,102,111,114,115,116,117,118,119,120,124,129,],[-57,-58,-60,-63,-64,-62,-59,-52,-53,-61,-48,122,-54,-44,-45,-46,-47,-49,-50,-51,-56,134,]),'ASCENDER':([29,30,31,32,33,52,53,79,124,136,],[-57,-58,-60,-63,-64,-62,-59,-61,-56,138,]),'DESCENDER':([29,30,31,32,33,52,53,79,124,136,],[-57,-58,-60,-63,-64,-62,-59,-61,-56,139,]),'NOT':([49,54,73,81,99,100,122,],[76,76,76,76,76,76,76,]),'VAR':([55,],[81,]),'LOG':([58,],[83,]),'AND':([77,111,],[99,-54,]),'OR':([77,111,],[100,-54,]),'LLLAVES':([92,101,127,137,],[113,113,113,113,]),'ELSE':([112,133,],[127,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,113,],[1,128,]),'asignacion':([0,113,],[2,2,]),'expresion':([0,22,37,73,113,],[3,50,63,50,3,]),'metodos':([0,113,],[4,4,]),'if':([0,113,],[6,6,]),'while':([0,113,],[7,7,]),'for':([0,113,],[8,8,]),'sort':([0,113,],[9,9,]),'include':([0,113,],[10,10,]),'valueOf':([0,113,],[11,11,]),'chartAt':([0,113,],[12,12,]),'push':([0,113,],[13,13,]),'slice':([0,113,],[14,14,]),'pop':([0,113,],[15,15,]),'concat':([0,113,],[16,16,]),'term':([0,22,34,35,36,37,73,113,],[18,18,60,61,62,18,18,18,]),'factor':([0,22,34,35,36,37,38,39,40,41,49,54,57,68,69,70,71,72,73,76,81,93,94,95,96,97,99,100,104,109,113,122,134,],[19,51,51,51,51,51,64,65,66,67,75,75,82,85,86,87,88,89,91,98,75,114,115,116,117,118,75,75,123,125,19,75,136,]),'imprimir':([0,113,],[20,20,]),'condicion':([49,54,73,81,99,100,122,],[74,80,90,102,119,120,129,]),'compuesta':([49,54,73,81,99,100,122,],[77,77,77,77,77,77,77,]),'then':([92,101,127,137,],[112,121,132,140,]),'else':([112,],[126,]),'instruccion':([134,],[135,]),}

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
  ('asignacion -> PALABRA ASIGNACION expresion','asignacion',3,'p_asignacion','YaccProyecto.py',116),
  ('expresion -> term MAS factor','expresion',3,'p_expresion_suma','YaccProyecto.py',121),
  ('expresion -> term MENOS factor','expresion',3,'p_expresion_resta','YaccProyecto.py',126),
  ('expresion -> term','expresion',1,'p_expression_term','YaccProyecto.py',131),
  ('expresion -> expresion PRODUCTO term','expresion',3,'p_expresion_producto','YaccProyecto.py',136),
  ('expresion -> expresion DIVISION term','expresion',3,'p_expresion_division','YaccProyecto.py',141),
  ('expresion -> expresion POTENCIA term','expresion',3,'p_expresion_potencia','YaccProyecto.py',146),
  ('expresion -> term MAYOR factor','expresion',3,'p_expresion_mayor','YaccProyecto.py',151),
  ('expresion -> term MENOR factor','expresion',3,'p_expresion_menor','YaccProyecto.py',156),
  ('condicion -> factor IGUAL factor','condicion',3,'p_condicion','YaccProyecto.py',162),
  ('condicion -> factor MAYOR factor','condicion',3,'p_condicion','YaccProyecto.py',163),
  ('condicion -> factor MENOR factor','condicion',3,'p_condicion','YaccProyecto.py',164),
  ('condicion -> factor ASIGNACION factor','condicion',3,'p_condicion','YaccProyecto.py',165),
  ('condicion -> NOT factor','condicion',2,'p_condicion','YaccProyecto.py',166),
  ('condicion -> factor DIFERENTE factor','condicion',3,'p_condicion','YaccProyecto.py',167),
  ('condicion -> compuesta AND condicion','condicion',3,'p_condicion','YaccProyecto.py',168),
  ('condicion -> compuesta OR condicion','condicion',3,'p_condicion','YaccProyecto.py',169),
  ('condicion -> compuesta','condicion',1,'p_condicion','YaccProyecto.py',170),
  ('condicion -> NEWLINE','condicion',1,'p_condicion','YaccProyecto.py',171),
  ('compuesta -> LPAREN condicion RPAREN','compuesta',3,'p_compuesta','YaccProyecto.py',176),
  ('term -> factor','term',1,'p_term_factor','YaccProyecto.py',180),
  ('factor -> NEW SET LPAREN LISTA RPAREN','factor',5,'p_factor_set','YaccProyecto.py',185),
  ('factor -> NUMERO','factor',1,'p_factor_num','YaccProyecto.py',190),
  ('factor -> FLOTANTE','factor',1,'p_factor_flot','YaccProyecto.py',195),
  ('factor -> PALABRA','factor',1,'p_factor_pal','YaccProyecto.py',200),
  ('factor -> STRING','factor',1,'p_factor_str','YaccProyecto.py',205),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor_expr','YaccProyecto.py',210),
  ('factor -> LISTA','factor',1,'p_factor_lista','YaccProyecto.py',215),
  ('factor -> BOOLEANO','factor',1,'p_factor_booleano','YaccProyecto.py',220),
  ('factor -> OBJETO','factor',1,'p_factor_objeto','YaccProyecto.py',225),
]
