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
```sql
SELECT * FROM tabla;
SELECT campo1, campo2 FROM tabla WHERE condicion;
```

### INSERT
```sql
INSERT INTO tabla (campo1, campo2) VALUES (valor1, valor2);
```

### UPDATE
```sql
UPDATE tabla SET campo = valor WHERE condicion;
```

### DELETE
```sql
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

```python
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

```bash
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
