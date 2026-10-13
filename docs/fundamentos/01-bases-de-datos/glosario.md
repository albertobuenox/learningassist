# Glosario — bases de datos

Definiciones de trabajo. Si una palabra de un enunciado no está aquí, búscalo en la documentación de PostgreSQL antes de pedir la solución.

## Modelo

### Base de datos relacional

Conjunto de tablas. Una fila es un hecho; una columna es un atributo de ese hecho. Las relaciones entre hechos se expresan con claves, no copiando bloques de texto.

### Tabla

Colección de filas con el mismo conjunto de columnas.

### Fila (tupla)

Un registro. En un diseño sano, cada fila se puede señalar con una clave y no significa dos cosas a la vez.

### Columna (atributo)

Un dato de la fila, con tipo: entero, texto, fecha, booleano, numérico. El tipo es parte del diseño.

### Dominio

El conjunto de valores legales de una columna. “Estado de la cita” no es “cualquier texto”: es un conjunto pequeño que tú fijas.

### Clave primaria

Columna o grupo de columnas que identifica una fila y no se repite ni queda vacío. Puede ser un entero generado o una clave natural (un ISBN), si de verdad es estable.

### Clave foránea

Columna que apunta a la clave primaria de otra tabla. Es la forma de decir “esta cita es de este paciente” sin copiar el nombre del paciente en cada cita.

### Cardinalidad

Cuántos de un lado se relacionan con cuántos del otro: uno a uno, uno a muchos, muchos a muchos. Muchos a muchos casi nunca se modela con una sola columna: hace falta una tabla intermedia.

### Integridad referencial

La base rechaza una cita cuyo paciente no existe, y define qué pasa si borras al paciente: prohibir el borrado, borrar en cascada o dejar la cita colgando. Elegir una de las tres es una decisión de negocio.

### Restricción

Regla que el motor obliga a cumplir: `NOT NULL`, `UNIQUE`, `CHECK`, clave foránea. Si la regla solo vive en la aplicación, otro cliente puede saltársela.

### Nulo

Ausencia de valor. No es cero ni cadena vacía. Comparar un nulo con `=` no da verdadero ni falso: hace falta `IS NULL`.

## Consulta

### SQL

Lenguaje para definir y manipular datos relacionales. Aquí importa el SQL que lee y escribe tu aplicación, no el dialecto de un producto concreto hasta que el ejercicio lo pida.

### `SELECT`

Pide un conjunto de filas. No “elige una variable”: describe el resultado.

### Proyección

Qué columnas aparecen en el resultado. `SELECT nombre` proyecta una columna.

### Selección (`WHERE`)

Qué filas pasan el filtro.

### Orden (`ORDER BY`)

El resultado no tiene orden garantizado si no lo pides. Dos ejecuciones pueden diferir.

### `JOIN`

Combina filas de dos tablas según una condición, casi siempre la clave foránea. `INNER JOIN` se queda con las parejas que coinciden. `LEFT JOIN` conserva las filas de la izquierda aunque no haya pareja a la derecha (las columnas derechas salen nulas).

### Agregación

Resume filas: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`. Tras agrupar, cada grupo es una fila del resultado.

### `GROUP BY`

Parte las filas en grupos antes de agregar. Toda columna del `SELECT` que no esté dentro de una función de agregación tiene que estar en el `GROUP BY`. Si no ves por qué, prueba a escribir a mano dos filas del mismo grupo con distinto valor en esa columna.

### `HAVING`

Filtro sobre grupos, después de agregar. `WHERE` filtra filas, antes de agrupar.

### Subconsulta

Un `SELECT` dentro de otro. A veces se lee mejor que un join; a veces al revés. El criterio es cuál puedes explicar en voz alta.

### Vista

Una consulta con nombre. No copia los datos: se calcula al leerla (salvo que sea materializada). Sirve para no repetir un join en diez sitios.

## Diseño

### Normalización

Organizar tablas para que cada hecho se guarde una vez. Reduce contradicciones: el teléfono del paciente no puede valer dos cosas distintas en dos citas.

### Primera forma normal

Cada celda un valor atómico. Nada de “lunes, martes” dentro de una columna si luego vas a buscar “¿hay hueco el martes?”.

### Segunda y tercera forma normal

Cada atributo depende de la clave, de toda la clave y solo de la clave. Si el nombre de la ciudad depende del código postal y no de la clave de la cita, la ciudad no vive en la tabla de citas.

### Desnormalizar

Copiar un dato a propósito para leer más rápido o simplificar un informe. Es una decisión posterior, medible, no el punto de partida.

### Transacción

Grupo de escrituras que se confirman juntas o no se confirman. O se anota la cita y se ocupa el hueco, o no ocurre ninguna de las dos cosas.

### ACID

Propiedades que se esperan de esa transacción: atómica, consistente, aislada, durable. En la práctica del día a día, “atómica” y “aislada” son las que evitan citas duplicadas cuando dos personas pulsan a la vez.

### Aislamiento

Qué ve una transacción del trabajo aún no confirmado de otra. Leer el nivel por defecto de tu motor y probar dos sesiones `psql` enseña más que memorizar los cuatro nombres.

### Índice

Estructura aparte que acelera búsquedas y ordenaciones, y ralentiza escrituras. No es una columna mágica: apunta a filas según una expresión.

### `EXPLAIN`

Pide al motor el plan: cómo piensa ejecutar la consulta. “Seq Scan” en una tabla diminuta es normal. En una tabla grande, con un filtro selectivo, es una pista.

### Migración

Cambio versionado del esquema (añadir tabla, columna, índice) que puedes aplicar en otro entorno y, si hace falta, revertir. El esquema no se edita “a mano en producción” sin dejar rastro.

## Motor

### PostgreSQL

Motor relacional de código abierto. En este curso es el de referencia.

### `psql`

Cliente de consola. Aprender cuatro órdenes (`\dt`, `\d tabla`, `\q`, y pegar SQL) basta para los ejercicios.

### SGBD / DBMS

El programa que guarda los datos y obliga las reglas: PostgreSQL, MySQL, SQLite. SQLite es un fichero; PostgreSQL es un servicio. Esa diferencia importa al llegar a Sistemas.
