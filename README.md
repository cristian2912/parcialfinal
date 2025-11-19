# parcial final

## PUNTO 1

# Gramática de Atributos para Lenguaje SQL CRUD

Este proyecto implementa una gramática de atributos formal para un mini-lenguaje que soporta operaciones CRUD (Create, Read, Update, Delete) de tipo SQL.

## Descripción

La gramática modela un lenguaje simplificado que permite realizar consultas SQL básicas mediante una estructura formal que incluye:

- Producciones gramaticales
- Atributos sintetizados para generación de código
- Reglas semánticas para construcción de sentencias SQL

## Estructura del Proyecto

```
punto1/
├── estructuras_gramatica.py    # Definición de clases base
├── gramatica_crud.py            # Implementación de la gramática
└── ejemplo_uso.py               # Ejemplo de uso
```

### Archivos

- **`estructuras_gramatica.py`**: Define las estructuras de datos (`Produccion`, `ReglaAtributo`, `GramaticaAtributos`)
- **`gramatica_crud.py`**: Contiene la función `generar_gramatica_crud()` que construye la gramática completa
- **`ejemplo_uso.py`**: Demuestra cómo instanciar y visualizar la gramática

## Operaciones Soportadas

El lenguaje soporta las siguientes operaciones SQL:

### SELECT
```
SELECT * FROM tabla;
SELECT campo1, campo2 FROM tabla WHERE condicion;
```

### INSERT
```
INSERT INTO tabla (campo1, campo2) VALUES (valor1, valor2);
```

### UPDATE
```
UPDATE tabla SET campo = valor WHERE condicion;
```

### DELETE
```
DELETE FROM tabla WHERE condicion;
```

## Características de la Gramática

### No Terminales
- `Prog`: Programa completo
- `Consulta`: Tipo de consulta (SELECT, INSERT, UPDATE, DELETE)
- `SelectC`, `InsertC`, `UpdateC`, `DeleteC`: Consultas específicas
- `OptWhere`: Cláusula WHERE opcional
- `LCampo`: Lista de campos
- `Campo`: Campo individual
- `Cond`: Condición lógica
- `Exp`: Expresión de comparación
- `Valor`: Valor literal

### Terminales
- Palabras clave: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `INTO`, `VALUES`, `SET`, `FROM`, `WHERE`, `AND`, `OR`
- Operadores: `*`, `,`, `=`, `(`, `)`, `;`
- Tokens: `ID` (identificador), `NUM` (número), `CAD` (cadena)

### Atributos

La gramática utiliza principalmente dos tipos de atributos:

- **`cod`**: Atributo sintetizado que almacena el código SQL generado
- **`lista`**: Atributo sintetizado para concatenar listas de campos

## Uso

```
from gramatica_crud import generar_gramatica_crud

# Generar la gramática
gramatica = generar_gramatica_crud()

# Acceder a los componentes
print(gramatica.no_terminales)
print(gramatica.terminales)
print(gramatica.producciones)
print(gramatica.atributos)
print(gramatica.reglas_atributos)
```

Para ejecutar el ejemplo completo:

```
python ejemplo_uso.py
```

## Ejemplo de Salida

El script de ejemplo muestra:

1. Lista de no terminales
2. Lista de terminales
3. Producciones de la gramática
4. Atributos por símbolo
5. Reglas semánticas de atributos

## Reglas Semánticas

Las reglas de atributos definen cómo se construye el código SQL. Por ejemplo:

```
SelectC → SELECT LCampo FROM ID OptWhere
SelectC.cod = "SELECT " + LCampo.lista + " FROM " + ID.lexema + OptWhere.cod
```

Cada regla especifica cómo calcular el atributo del lado izquierdo a partir de los atributos de los símbolos en el lado derecho.


## PUNTO 2

# Parser para Lenguaje de Operaciones Matriciales

Este proyecto implementa un analizador léxico y sintáctico (parser) para un lenguaje de programación diseñado específicamente para realizar operaciones matriciales, incluyendo el producto punto entre matrices de diferentes dimensiones.

## Descripción del Problema

El objetivo es diseñar una gramática para un lenguaje de programación capaz de resolver el producto punto entre dos matrices de diferentes dimensiones, validando la sintaxis de declaraciones de matrices y expresiones aritméticas que las involucran.

## Gramática del Lenguaje

La gramática formal del lenguaje se define como:

```
Prog     → DeclList StmtList

DeclList → Decl DeclList
DeclList → ε

Decl     → mat id '[' num ',' num ']' ';'

StmtList → Stmt StmtList
StmtList → ε

Stmt     → Assign ';'

Assign   → id '=' Expr

Expr     → Expr '+' Term
Expr     → Expr '-' Term
Expr     → Term

Term     → Term '*' Factor
Term     → Factor

Factor   → id
Factor   → '(' Expr ')'
```

## Características del Lenguaje

### Declaración de Matrices

Las matrices se declaran usando la palabra clave `mat` seguida de un identificador y las dimensiones:

```
mat A[2,3];
mat B[3,4];
mat C[2,4];
```

Formato: `mat identificador[filas,columnas];`

### Operaciones Soportadas

- **Producto matricial** (`*`)
- **Suma** (`+`)
- **Resta** (`-`)
- **Agrupación con paréntesis** `( )`

### Asignaciones

```
C = A * B;
C = A * B + C;
resultado = (A + B) * C;
```

## Estructura del Proyecto

```
punto2/
├── gramatica.txt           # Gramática formal del lenguaje
├── main.py                 # Implementación del lexer y parser
├── programa_ejemplo.txt    # Ejemplo de código válido
└── programa_error.txt      # Ejemplo de código con errores
```

## Componentes de la Implementación

### 1. Lexer (Analizador Léxico)

Transforma el código fuente en una secuencia de tokens:

- **MAT**: Palabra clave `mat`
- **ID**: Identificadores (nombres de matrices)
- **NUM**: Números literales
- **Símbolos**: `[`, `]`, `,`, `;`, `=`, `+`, `-`, `*`, `(`, `)`
- **EOF**: Fin de archivo

### 2. Parser (Analizador Sintáctico)

Implementa un parser descendente recursivo que valida la estructura sintáctica del programa según la gramática definida.

**Métodos principales:**
- `parse_program()`: Punto de entrada, valida el programa completo
- `_DeclList()`: Procesa la lista de declaraciones de matrices
- `_Decl()`: Valida una declaración individual
- `_StmtList()`: Procesa la lista de sentencias
- `_Stmt()`: Valida una sentencia (asignación)
- `_Assign()`: Procesa asignaciones
- `_Expr()`: Analiza expresiones con suma y resta
- `_Term()`: Analiza términos con multiplicación
- `_Factor()`: Procesa factores (identificadores o expresiones entre paréntesis)

### 3. Token

Clase que representa un token con:
- `tipo`: Tipo del token (MAT, ID, NUM, etc.)
- `lexema`: Texto literal del token
- `pos`: Posición en el código fuente

## Uso

### Ejecución Básica

```
python main.py
```

El programa lee automáticamente el archivo `programa_error.txt` y valida su sintaxis.

### Cambiar el Archivo de Entrada

Modifica la línea en `main.py`:

```
codigo = leer_archivo("programa_ejemplo.txt")  # o cualquier otro archivo
```

### Ejemplo de Programa Válido

```
mat A[2,3];
mat B[3,4];
mat C[2,4];

C = A * B;
C = A * B + C;
```

**Salida:**
```
El programa ES válido según la gramática.
```

### Ejemplo de Programa con Errores

```
mat A[2,3]
mat B[3,4];

A = A * ;
```

**Salida:**
```
ERROR DE SINTAXIS:
Se esperaba ';' pero llegó 'mat' en posición 11
```

## Reglas de Precedencia

El parser implementa la precedencia estándar de operadores:

1. **Mayor precedencia**: `*` (multiplicación matricial)
2. **Menor precedencia**: `+`, `-` (suma y resta)
3. Los paréntesis modifican el orden de evaluación

### Ejemplos de Precedencia

```
A = B + C * D;     # Equivale a: A = B + (C * D)
A = (B + C) * D;   # Multiplicación después de suma
```

## Manejo de Errores

El parser proporciona mensajes de error descriptivos que incluyen:

- Token esperado vs. token recibido
- Posición exacta del error en el código fuente
- Contexto del error (lexema)

### Tipos de Errores Detectados

1. **Errores léxicos**: Caracteres no reconocidos
2. **Errores sintácticos**: Estructura incorrecta del programa
3. **Tokens faltantes**: Punto y coma, paréntesis, etc.
4. **Tokens inesperados**: Símbolos en posiciones incorrectas


## PUNTO 3

# Parser ANTLR para Lenguaje de Operaciones Matriciales

Implementación en ANTLR de una gramática para un lenguaje de programación capaz de resolver operaciones matriciales, incluyendo el producto punto entre matrices de diferentes dimensiones.

## Descripción

Este proyecto reimplementa la gramática del lenguaje matricial utilizando ANTLR 4.13.1 como generador de parsers, con Python como lenguaje objetivo. ANTLR genera automáticamente el analizador léxico, sintáctico y las estructuras necesarias para procesar programas escritos en este lenguaje.

## Tecnologías

- **ANTLR 4.13.1**: Generador de parsers
- **Python 3.x**: Lenguaje objetivo
- **antlr4-python3-runtime**: Runtime de ANTLR para Python

## Estructura del Proyecto

```
punto3/
├── Matrices.g4              # Gramática ANTLR (fuente principal)
├── MatricesLexer.py         # Lexer generado automáticamente
├── MatricesParser.py        # Parser generado automáticamente
├── MatricesListener.py      # Listener generado (patrón observer)
├── MatricesLexer.tokens     # Definición de tokens (lexer)
├── Matrices.tokens          # Definición de tokens (parser)
├── MatricesLexer.interp     # Metadata del lexer
├── Matrices.interp          # Metadata del parser
├── run_matrices.py          # Script de ejecución
└── programa_ejemplo.txt     # Programa de prueba
```

## Gramática (Matrices.g4)

### Sintaxis

```
prog      : declList stmtList EOF ;

declList  : decl declList | ;
decl      : MAT ID '[' NUM ',' NUM ']' ';' ;

stmtList  : stmt stmtList | ;
stmt      : assign ';' ;
assign    : ID '=' expr ;

expr      : expr '+' term
          | expr '-' term
          | term ;

term      : term '*' factor
          | factor ;

factor    : ID
          | '(' expr ')' ;
```

### Léxico

```
MAT    : 'mat' ;
ID     : [a-zA-Z_] [a-zA-Z_0-9]* ;
NUM    : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ;

Símbolos: [ ] , ; = + - * ( )
```

## Archivos Generados

ANTLR genera automáticamente:

- **MatricesLexer.py**: Tokenizador del código fuente
- **MatricesParser.py**: Analizador sintáctico con las 9 reglas de la gramática
- **MatricesListener.py**: Clase base para recorrer el árbol sintáctico
- **Archivos .tokens**: Mapeo de tokens a valores numéricos
- **Archivos .interp**: Metadata para interpretación

## Instalación

### Requisitos

```
pip install antlr4-python3-runtime
```

### Generar el Parser (opcional)

Si se modifica `Matrices.g4`:

```
# Descargar ANTLR
curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar

# Generar archivos Python
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 Matrices.g4
```

## Uso

### Ejecutar el Analizador

```
python run_matrices.py                    # Analiza programa_ejemplo.txt
python run_matrices.py mi_programa.txt    # Analiza archivo específico
```

### Ejemplo de Programa

```
mat A[2,3];
mat B[3,4];
mat C[2,4];

C = A * B;
C = A * B + C;
```

Salida:
```
El programa 'programa_ejemplo.txt' ES válido según la gramática.
```

## Script Principal (run_matrices.py)

```
import sys
from antlr4 import FileStream, CommonTokenStream
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser

def analizar_archivo(ruta):
    input_stream = FileStream(ruta, encoding="utf-8")
    lexer = MatricesLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MatricesParser(tokens)
    parser.removeErrorListeners()
    
    tree = parser.prog()
    print(f"\nEl programa '{ruta}' ES válido según la gramática.\n")
    return tree

ruta_por_defecto = "programa_ejemplo.txt"
if len(sys.argv) >= 2:
    ruta_por_defecto = sys.argv[1]

analizar_archivo(ruta_por_defecto)
```

## Ventajas de ANTLR

Comparado con el parser manual del punto 2

| Aspecto | Parser Manual | ANTLR |
|---------|---------------|-------|
| Líneas de código | ~150 | ~60 (gramática) |
| Recursión izquierda | Transformación manual requerida | Manejada automáticamente |
| Árbol sintáctico | Construcción manual | Generado automáticamente |
| Mantenimiento | Cambios requieren modificar código | Solo editar gramática |
| Mensajes de error | Implementación manual | Sistema robusto incluido |

ANTLR maneja automáticamente la recursión izquierda directa en reglas como:

```
expr : expr '+' term  // No requiere transformación
     | term ;
```

## Tokens Reconocidos

```
MAT=1     ID=2      NUM=3      WS=4
LBRACK=5  RBRACK=6  COMMA=7    SEMI=8
ASSIGN=9  PLUS=10   MINUS=11   STAR=12
LPAREN=13 RPAREN=14
```

## Extensiones Implementables

### Intérprete con Listener

```
class InterpretadorMatrices(MatricesListener):
    def __init__(self):
        self.matrices = {}
    
    def exitDecl(self, ctx):
        nombre = ctx.ID().getText()
        filas = int(ctx.NUM(0).getText())
        cols = int(ctx.NUM(1).getText())
        self.matrices[nombre] = crear_matriz(filas, cols)
```

### Análisis Semántico

- Validación de dimensiones en operaciones
- Verificación de declaraciones previas
- Chequeo de tipos

### Generación de Código

```
class GeneradorNumPy(MatricesListener):
    def exitAssign(self, ctx):
        # Generar código NumPy equivalente
        pass
```

## Manejo de Errores

ANTLR proporciona manejo automático. Para personalizar:

```
from antlr4.error.ErrorListener import ErrorListener

class ErrorPersonalizado(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error línea {line}:{column} - {msg}")
```
