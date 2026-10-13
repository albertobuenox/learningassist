---
tags:
  - bases-de-datos
  - ejercicio
  - medio
---

# 04 — Diseño y normalización

!!! info "Antes de empezar"

    Tiempo: 60–90 minutos.

??? tip "Pista"

    Apoyo: CS50 SQL, lección de diseño. Glosario: formas normales, [desnormalizar.](../glosario.md#desnormalizar)

Te pasan esta tabla. “Funciona”: la aplicación lee de aquí el recibo.

| recibo_id | fecha | cliente | correo_cliente | ciudad_cliente | lineas | total |

| --- | --- | --- | --- | --- | --- | --- |

| 10 | 2026-04-02 | Ana Ruiz | ana@correo.test | Valencia | "2 x Café; 1 x Té" | 7.50 |

| 11 | 2026-04-02 | Ana Ruiz | ana.ruiz@correo.test | Valencia | "1 x Café" | 2.00 |

`lineas` es un texto. El correo de Ana no coincide en las dos filas. El total está guardado y también se podría calcular.

## Qué hacer

1. Lista los hechos distintos que hay mezclados en una sola fila (cliente, recibo, línea, producto).
2. Propón tablas separadas. Cada hecho una vez. El producto tiene nombre y un precio de catálogo; la línea guarda el precio cobrado.
3. Para cada anomalía de los datos de ejemplo, di si tu esquema la hace imposible o solo más incómoda.
4. El negocio quiere el nombre del cliente impreso en el recibo aunque mañana cambie de nombre en la ficha. ¿Copias el nombre en el recibo? Justifica la copia o la ausencia de copia. Eso es desnormalizar a propósito, o no hacerlo.

!!! warning "Restricciones"

    - No añadas puntos de fidelización ni impuestos. El problema ya es bastante.
    - Puedes quedarte en diagrama. Si creas las tablas, mete los dos recibos de ejemplo y comprueba que no hace falta repetir el correo para tener las dos compras de Ana.

!!! success "Cómo sabes que está bien"

    - ¿Puedes cambiar el correo de Ana en un solo sitio y que las dos compras sigan siendo suyas?
    - ¿Puedes contar cuántos cafés se vendieron el 2 de abril sin trocear un texto?
    - ¿El total del recibo puede discrepar de la suma de las líneas? Si lo guardas, ¿quién manda cuando discrepen?
