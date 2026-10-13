---
tags:
  - corto
  - ejercicio
  - http
---

# 03 — Repetir la petición

!!! info "Antes de empezar"

    Tiempo: 45 minutos. Sin código nuevo obligatorio. Glosario: [seguro](../glosario.md#seguro), [idempotente](../glosario.md#idempotente).

??? tip "Pista"

    Antes de pelear con el enunciado, lee en el glosario: [seguro](../glosario.md#seguro), [idempotente](../glosario.md#idempotente).

## Tabla

Para cada fila, escribe qué debería pasar la segunda vez si la primera tuvo éxito, y qué método usarías. Luego mira si tu servidor actual (el de productos o el de facturas) cumple esa frase. Si no la cumple, anota el desvío. No lo arregles todavía salvo que el arreglo sea de una línea y lo entiendas.

| Acción | Método que eliges | ¿Seguro? | ¿Idempotente? | Qué observas al repetir |
| --- | --- | --- | --- | --- |
| Ver la lista de productos | | | | |
| Crear un producto | | | | |
| Cambiar el precio de un producto a 3.00 | | | | |
| Borrar el producto 4 | | | | |
| “Cancelar cita” como enlace que el usuario abre | | | | |

La última fila es una trampa de diseño. Un enlace es un `GET`. Decide si cancelar puede ser un enlace.

!!! success "Cómo sabes que está bien"

    - Ninguna fila deja el método en blanco.
    - Puedes explicar por qué crear no es idempotente y borrar sí, con un ejemplo de dos llamadas seguidas.
    - Si tu servidor crea dos productos al repetir el `POST`, lo has escrito como hecho observado, no como teoría.
