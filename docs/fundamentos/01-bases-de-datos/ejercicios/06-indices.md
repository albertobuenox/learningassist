---
tags:
  - bases-de-datos
  - ejercicio
  - medio
---

# 06 — Índices

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos. Lectura: https://use-the-index-luke.com/ (el capítulo de la cláusula `WHERE` basta para empezar).

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

Genera una tabla grande. Un bucle en SQL o un script corto: del orden de 100.000 filas en `eventos (id, usuario_id, tipo, creado_en)`. `usuario_id` entre 1 y 500. `tipo` con unos pocos valores, uno de ellos muy frecuente.

## Tareas

1. Esta consulta, sin índices extra:

   `SELECT * FROM eventos WHERE usuario_id = 42 ORDER BY creado_en DESC LIMIT 20`

   Mira `EXPLAIN ANALYZE`. Anota si hay recorrido secuencial y el tiempo aproximado.
2. Propón **un** índice. Créalo. Vuelve a explicar. ¿Cambió el plan? Si no cambió, ¿la tabla te parece pequeña para que al motor le importe, o el índice no cubre el filtro y el orden?
3. Un segundo experimento: `WHERE tipo = 'el-valor-que-casi-todas-las-filas-tienen'`. ¿Un índice en `tipo` ayuda? Si no, explica con tus palabras qué tiene de poco selectivo ese filtro.
4. Inserta otras 10.000 filas con el índice puesto y sin él (puedes medirlo en una copia de la tabla). No hace falta un benchmark de laboratorio: basta con ver que escribir también paga el índice.

!!! success "Cómo sabes que está bien"

    - No creas un índice por columna “por si acaso”. En el archivo queda escrito, para cada índice, qué consulta gana y qué operación pierde.
    - Sabes distinguir “el plan usa el índice” de “la consulta es correcta”. Un plan rápido que filtra el usuario equivocado sigue mal.
    - Si `EXPLAIN` te desconcierta, copia el nodo que no entiendas y busca ese nombre en el manual. Anota la frase del manual que te encajó, no un índice al azar.
