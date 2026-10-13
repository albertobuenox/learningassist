---
tags:
  - ejercicio
  - frontend
  - largo
---

# 07 — Datos remotos

!!! info "Antes de empezar"

    Tiempo: 3 horas.

??? tip "Pista"

    Apoyo: javascript.info sobre `fetch` y la documentación de React sobre efectos. El servidor puede ser el del ejercicio 3.

## Pantalla

Al abrir, la lista de productos sale de `GET /productos`.

Tres situaciones, dibujadas de verdad (un párrafo visible basta, no hace falta ilustración):

- cargando, antes de que llegue la respuesta;
- vacío, si el array llega con longitud cero;
- error, si la red falla o el estado no es 200, con el código si lo tienes.

Un botón “Reintentar” solo aparece en el error y vuelve a pedir.

!!! warning "Restricciones"

    - Mira `response.ok` o el código. No des por buena una respuesta 500 con cuerpo vacío.
    - Si el componente se desmonta antes de que la promesa resuelva, no actualices estado de un componente que ya no está. La forma actual recomendada cambia con la versión de React: busca “fetch data” en la documentación vigente y cita en un comentario qué patrón usaste.
    - La URL base está en una constante. No repartida por tres archivos.

!!! success "Cómo sabes que está bien"

    - Paras el servidor y recargas. ¿Ves el error, o un spinner eterno?
    - Respondes `[]` (puedes forzarlo un momento). ¿Ves el vacío, o una tabla sin filas que parece rota?
    - En la pestaña de red hay **una** petición al cargar, o sabes explicar por qué en desarrollo aparecen dos (Strict Mode) y por qué tu UI no duplica productos por eso.
