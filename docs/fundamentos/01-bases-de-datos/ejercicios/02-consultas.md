---
tags:
  - bases-de-datos
  - ejercicio
  - medio
---

# 02 — Consultas

!!! info "Antes de empezar"

    `SELECT`, filtro, orden y nulos. Tiempo: 60–90 minutos. Crea estas tablas en PostgreSQL e inserta filas suficientes para que cada pregunta tenga una respuesta interesante. Inventa los datos. Incluye al menos un precio nulo y un producto sin categoría. ```sql -- Punto de partida. No es la solución de las preguntas. CREATE TABLE categorias ( id integer PRIMARY KEY, nombre text NOT NULL ); CREATE TABLE productos ( id integer PRIMARY KEY, nombre text NOT NULL, categoria_id integer REFERENCES categorias (id), precio numeric(10, 2), activo boolean NOT NULL ); ```

??? tip "Pista"

    Si hace falta: SQLBolt, lecciones de `SELECT`, `WHERE` y `ORDER BY`.

## Preguntas

Escribe una consulta por apartado. Guárdalas en un archivo `.sql`.

1. Productos activos, del más caro al más barato. Los que no tienen precio van al final, no al principio. ¿Qué cláusula decide ese orden?
2. Productos sin categoría. ¿Por qué `categoria_id = NULL` no sirve?
3. Productos cuyo nombre contiene `café`, sin distinguir mayúsculas, y que cuestan menos de 10.
4. Las tres categorías con más productos activos. Si hay empate en el tercer puesto, anota qué hace tu consulta y si te parece aceptable.
5. Una consulta que devuelva mal el resultado a propósito: cuenta productos por categoría y pierde las categorías vacías. En un comentario, di qué unión lo arreglaría. No hace falta escribir aún el arreglo si el ejercicio 3 es el siguiente; sí hace falta saber por qué se pierden.

!!! success "Cómo sabes que está bien"

    Ejecuta cada consulta y mira las filas.

    - ¿El número de filas es el que esperabas antes de ejecutar, o lo ajustaste después de ver el resultado?
    - Quita el `ORDER BY` de la primera. ¿Sigue siendo válida como “del más caro al más barato”?
    - ¿Hay algún producto inactivo colándose? Si sí, el filtro está en el sitio equivocado.
