---
tags:
  - bases-de-datos
  - corto
  - ejercicio
---

# 01 — Modelo en papel

!!! info "Antes de empezar"

    Antes de SQL. Papel, tablet o un diagrama. Tiempo: 45–90 minutos. Curso si te atascas: CS50 SQL, lección de diseño; glosario: clave, cardinalidad, tabla intermedia.

??? tip "Pista"

    Si te atascas, abre el [glosario](../glosario.md) de la asignatura y el README antes de un curso largo. Una sola entrada suele desbloquear el enunciado.

## Situación

Una biblioteca de barrio presta libros. Reglas que te han contado en voz alta, no un esquema:

- Un libro tiene título, año y un ISBN que no se repite.
- Un libro puede tener varios autores. Un autor escribe varios libros.
- Hay varios ejemplares físicos del mismo libro. Cada ejemplar tiene un código de barras.
- Un socio tiene nombre y correo, que tampoco se repite.
- Un préstamo es un socio, un ejemplar, la fecha de salida y la fecha de devolución. La devolución puede no haber ocurrido.
- Un ejemplar no puede estar en dos préstamos abiertos a la vez. “Abierto” significa que aún no hay fecha de devolución.

## Qué entregar

Un diagrama con cajas, columnas y el tipo de relación (1–N, N–N). Marca clave primaria y foránea. En un párrafo, explica dónde vive la regla del ejemplar que no puede prestarse dos veces.

!!! warning "Restricciones"

    - No abras un cliente SQL en este ejercicio.
    - No metas el nombre del autor como texto dentro de la tabla de libros si un libro puede tener varios.
    - No inventes “multas” ni “reservas”. El alcance es el de arriba.

!!! success "Cómo sabes que está bien"

    - ¿Puedes señalar la fila que identifica un ejemplar concreto, distinta de la fila que identifica la obra?
    - Si Ana y Luis escriben el mismo libro, ¿en cuántos sitios está escrito el nombre de Ana?
    - Si borras un socio con un préstamo abierto, ¿qué debería negarse el sistema a hacer, y dónde lo has anotado?
    - ¿Tu diagrama permite un préstamo ya devuelto y, a la vez, impide dos abiertos del mismo ejemplar? Si la segunda regla no cabe en una clave única simple, dilo: a veces la regla no es solo una `UNIQUE`.

    Cuando el diagrama aguante esas cuatro preguntas, pásalo a tablas en el ejercicio 7 o, si quieres práctica guiada antes, sigue con el 2.
