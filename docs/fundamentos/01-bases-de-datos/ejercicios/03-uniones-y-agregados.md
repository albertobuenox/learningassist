---
tags:
  - bases-de-datos
  - ejercicio
  - medio
---

# 03 — Uniones y agregados

!!! info "Antes de empezar"

    Tiempo: 90 minutos.

??? tip "Pista"

    Apoyo: SQLBolt (joins y `GROUP BY`) y, si quieres más, una categoría de https://pgexercises.com/ sin mirar la solución.

Extiende el esquema del ejercicio 2. No borres lo anterior.

```sql

CREATE TABLE pedidos (

id integer PRIMARY KEY,

creado_en date NOT NULL

);

CREATE TABLE lineas (

id integer PRIMARY KEY,

pedido_id integer NOT NULL REFERENCES pedidos (id),

producto_id integer NOT NULL REFERENCES productos (id),

cantidad integer NOT NULL CHECK (cantidad > 0),

precio_unitario numeric(10, 2) NOT NULL

);

```

Datos mínimos: un pedido con dos líneas, un pedido sin líneas, un producto que nadie ha comprado, una línea cuyo precio unitario no coincida con el precio actual del producto.

## Preguntas

1. Cada pedido con su número de líneas y el importe (`cantidad * precio_unitario`). Los pedidos sin líneas deben salir, con cero líneas. ¿Inner o left, y desde qué tabla?
2. El importe usa el precio **de la línea**, no el precio actual del producto. Escribe la consulta correcta y, en un comentario, la consulta tentadora que daría un total distinto. ¿Cuál de las dos responde a “¿cuánto pagó el cliente”?
3. Productos que no aparecen en ninguna línea. Resuélvelo de dos maneras (una con `JOIN` y filtro de nulos, otra con `NOT EXISTS` o `NOT IN`). ¿En cuál te fías más si `producto_id` pudiera ser nulo?
4. Importe total por categoría, solo categorías con más de 50 de importe. ¿El filtro de “más de 50” va en `WHERE` o en `HAVING`? Prueba el otro y anota el error o el resultado equivocado.
5. El producto más vendido por unidades. Define qué haces si hay empate y deja esa decisión escrita junto a la consulta.

!!! success "Cómo sabes que está bien"

    - ¿Una categoría sin ventas desaparece en la pregunta 4? Decídelo y que la consulta obedezca tu decisión.
    - Cambia una cantidad a 0 en los datos saltándote el `CHECK` (no deberías poder). Si puedes, la tabla no tiene la regla.
    - Explica en voz alta, señalando una fila concreta, por qué el pedido vacío no desaparece en la pregunta 1.
