import sys
from antlr4 import FileStream, CommonTokenStream
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser


def analizar_archivo(ruta):
    """
    Analiza un programa de matrices usando la gramática ANTLR.

    Si la sintaxis es correcta, imprime un mensaje de éxito.
    Si hay error, deja que ANTLR lance la excepción correspondiente.
    """
    input_stream = FileStream(ruta, encoding="utf-8")
    lexer = MatricesLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MatricesParser(tokens)

    # lanza excepción en el primer error de sintaxis
    parser.removeErrorListeners()  # quitar listeners por defecto

    tree = parser.prog()  # regla inicial
    print(f"\nEl programa '{ruta}' ES válido según la gramática.\n")
    return tree


#  EJEMPLO DE USO
ruta_por_defecto = "programa_ejemplo.txt"
if len(sys.argv) >= 2:
    ruta_por_defecto = sys.argv[1]

analizar_archivo(ruta_por_defecto)
